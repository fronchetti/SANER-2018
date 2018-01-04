try:
    import os
    import json
    import csv
    from datetime import datetime
except ImportError as error:
    raise ImportError(error)

dataset = './Dataset/'
folders = os.listdir(dataset)

def get_pulls(json):
    opened, closed, merged = [], [], []
    for pull in json:       
        if pull['closed_at'] is None:
            opened.append(pull)
        else:
            if pull['merged_at'] is None:
                closed.append(pull)
            else:
                merged.append(pull)
    return opened, closed, merged

def get_about(json):
    stars = json['stargazers_count']
    forks = json['forks_count']
    url = json['html_url']
    language = json['language']
    age = 2017 - int(datetime.strptime(json['created_at'], '%Y-%m-%dT%H:%M:%SZ').date().year)
    
    return stars, forks, url, language, age

def get_languages(json):
    languages = []
    if json:
        for language in json:
            languages.append(language.encode('ascii','ignore'))
    return languages

def get_loc(json):
    if 'R' in json:
        return json['R']['code'], json['SUM']['code']
    else:
        return 0, json['SUM']['code']

def main():
    projects = {}
    
    for project in folders:
        folder = dataset + project

        if os.path.isdir(folder):
            projects[project] = {}

            if os.path.isfile(folder + '/about.json'):
                about_file = json.load(open(folder + '/about.json', 'r'))
                
                if about_file:                                                                                                
                    projects[project]['stars'], projects[project]['forks'], projects[project]['url'], projects[project]['main_language'], projects[project]['age'] = get_about(about_file)

            if os.path.isfile(folder + '/languages.json'):
                languages_file = json.load(open(folder + '/languages.json', 'r'))
                projects[project]['languages'] = get_languages(languages_file)
                
            if os.path.isfile(folder + '/loc.json'):
                print project
                loc_file = json.load(open(folder + '/loc.json', 'r'))
                projects[project]['loc_r'], projects[project]['loc_total'] = get_loc(loc_file)

            if os.path.isfile(folder + '/commits.csv'):
                commits_file = open(folder + '/commits.csv', 'r')
                commits_count = num_lines = sum(1 for line in commits_file)
                projects[project]['commits'] = commits_count
            else:
                projects[project]['commits'] = 0
            
            if os.path.isfile(folder + '/newcomers.csv'):
                newcomers_file = open(folder + '/newcomers.csv', 'r')
                newcomers_count = num_lines = sum(1 for line in newcomers_file)
                projects[project]['newcomers'] = newcomers_count
            else:
                projects[project]['newcomers'] = 0
                            
            if os.path.isfile(folder + '/pulls.json'):
                pulls_file = json.load(open(folder + '/pulls.json', 'r'))
                pulls_opened, pulls_closed, pulls_merged = get_pulls(pulls_file)
                projects[project]['pulls_opened'] = len(pulls_opened)
                projects[project]['pulls_closed'] = len(pulls_closed)
                projects[project]['pulls_merged'] = len(pulls_merged)                   
            else:
                projects[project]['pulls_opened'] = 0
                projects[project]['pulls_closed'] = 0
                projects[project]['pulls_merged'] = 0           
                            
    with open('summary.csv', 'w') as csv_file:
        fieldnames = ['project', 'url', 'main_language', 'languages', 'age', 'stars', 'forks', 'commits', 'newcomers', 'pulls_opened', 'pulls_closed', 'pulls_merged', 'loc_r', 'loc_total',]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        
        for project in projects:
            project_name = project
            project = projects[project]
            if len(fieldnames) == len(project) + 1:
                    writer.writerow({'project': project_name, 'url': project['url'], 'main_language': project['main_language'], 'languages': project['languages'], 'age': project['age'], 'stars': project['stars'], 'forks': project['forks'], 'commits': project['commits'], 'newcomers': project['newcomers'], 'pulls_opened': project['pulls_opened'], 'pulls_closed': project['pulls_closed'], 'pulls_merged': project['pulls_merged'], 'loc_r': project['loc_r'], 'loc_total': project['loc_total']})
            else:
                print project_name
                print project
main()
    
