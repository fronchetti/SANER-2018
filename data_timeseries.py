try:
    import os
    import json
    import csv
    import numpy
    import Crawler.crawler as GitCrawler
    from datetime import datetime
except ImportError as error:
    raise ImportError(error)

dataset = './Dataset/'
folders = os.listdir(dataset)

def project_monthly_contributions(list):
    commits = {}
    
    for commit in list:
        date = datetime.strptime(commit.strip(), '%Y-%m-%d').date()
        
        # There is not a significant number of projects with commits before 2008
        # Then, we ignore commits before this year.
        if date.year > 2007:
			# Group the date by quarters
			if date.month < 4:
			   date = date.replace(day = 15, month = 3)
			if date.month > 3 and date.month < 7:
			   date = date.replace(day = 15, month = 6)
			if date.month > 6 and date.month < 10:
			   date = date.replace(day = 15, month = 9)
			if date.month > 9:
			   date = date.replace(day = 15, month = 12)

			# Quantifies the amount of commits in a quarter
			if date in commits:
				commits[date] = commits[date] + 1
			else:
				commits[date] = 1

    return commits
        
def get_commits_from_pulls(project, folder):
	commits_from_pulls = []
	
	if os.path.isfile(folder + '/pulls.json'):
		pulls_file = json.load(open(folder + '/pulls.json', 'r'))
	else:
		return []
	
	for pull in pulls_file:
		if pull['merged_at']:
			pull_commits_url = pull['_links']['commits']['href'].replace('https://api.github.com/','')
			pull_commits = crawler.request(pull_commits_url)
			
			for commit in pull_commits:
				sha = commit['sha']
				commits_from_pulls.append(sha)

	return commits_from_pulls

def main():
    projects_commits = {} # Dictionary of all projects commits

    for project in folders:
        folder = dataset + project
        commits_from_pulls = get_commits_from_pulls(project, folder) # We remove commits from pull requets
        # by identifying their hash on GitHub API
        
        if os.path.isfile(folder + '/commits.csv'):
            commits_file = open(folder + '/commits.csv', 'r')
            next(commits_file) # Ignore headers
            commits_file_data = csv.reader(commits_file)
            commits = []
			
            for commit in commits_file_data:
				commit_sha = commit[1].strip()
				commit_date = commit[0].strip()
				
				# If commit's hash is a hash from a pull request's commit
				# Then, ignore this commit.
				if commit_sha not in commits_from_pulls:
					commits.append(commit_date)

            commits = project_monthly_contributions(commits) # Count the number of commits per quarter in a project
            
            # We group the quarters of all projects in a dictionary of lists.
            # A list for each quarter.
            for date in commits:
                if date in projects_commits:
                    projects_commits[date] = projects_commits[date] + [commits[date]]
                else:
                    projects_commits[date] = [commits[date]]
        else:
            print(project + " does not contain a commits file.")

    with open('monthly_contributions.csv', 'w') as csv_file:
        fieldnames = ['Date', 'Amount', 'Mean', 'Median', 'Projects']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        
        for date in projects_commits:
			# Considering all the projects that have commits in this quarter:
            amount = sum(projects_commits[date]) # Number of commits in this quarter 
            mean = numpy.mean(projects_commits[date]) # Mean of commits in this quarter
            median = numpy.median(projects_commits[date]) # Median of commits in this quarter
            number_of_projects = len(projects_commits[date]) # Number of projects in this quarter
            writer.writerow({'Date': date, 'Amount': amount, 'Mean': mean, 'Median': median, 'Projects': number_of_projects})
         
api_client_id = '4161a8257efaea420c94' # Please, specify your own client id
api_client_secret = 'd814ec48927a6bd62c55c058cd028a949e5362d4' # Please, specify your own client secret
crawler = GitCrawler.Crawler(api_client_id, api_client_secret)
main()
