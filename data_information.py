import os
import json
import csv
from datetime import datetime

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

def get_stars(json):
	if json is None:
		json = []
	return json

def get_forks(json):
	if json is None:
		json = []
	return json

def main():
	projects = {}
	
	for project in folders:		
		projects[project] = {}
		folder = dataset + project

		if os.path.isdir(folder):
			if os.path.isfile(folder + '/about.json'):
				about_file = json.load(open(folder + '/about.json', 'r'))
				
				if about_file is None:
					continue
											
				projects[project]['stars'] = about_file['stargazers_count']
				projects[project]['forks'] = about_file['forks_count']
				projects[project]['language'] = about_file['language']
				projects[project]['age'] = 2017 - int(datetime.strptime(about_file['created_at'], '%Y-%m-%dT%H:%M:%SZ').date().year)

			if os.path.isfile(folder + '/commits.csv'):
				commits_file = open(folder + '/commits.csv', 'r')
				commits_count = num_lines = sum(1 for line in commits_file)
				projects[project]['commits'] = commits_count
			else:
				print project
				projects[project]['commits'] = 0
			
			if os.path.isfile(folder + '/newcomers.csv'):
				newcomers_file = open(folder + '/newcomers.csv', 'r')
				newcomers_count = num_lines = sum(1 for line in newcomers_file)
				projects[project]['newcomers'] = newcomers_count
			else:
				print project
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
				
			'''
			if os.path.isfile(folder + '/stars.json'):
				stars_file = json.load(open(folder + '/stars.json', 'r'))
				stars = get_stars(stars_file)

			if os.path.isfile(folder + '/forks.json'):
				forks_file = json.load(open(folder + '/forks.json', 'r'))
				forks = get_forks(forks_file)
			'''
			
	with open('summary.csv', 'w') as csv_file:
		fieldnames = ['project', 'language', 'age', 'stars', 'forks', 'commits', 'newcomers', 'pulls_opened', 'pulls_closed', 'pulls_merged']
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		writer.writeheader()
		
		for project in projects:
			project_name = project
			project = projects[project]
			if len(project) == 9:
				writer.writerow({'project': project_name, 'language': project['language'], 'age': project['age'], 'stars': project['stars'], 'forks': project['forks'], 'commits': project['commits'], 'newcomers': project['newcomers'], 'pulls_opened': project['pulls_opened'], 'pulls_closed': project['pulls_closed'], 'pulls_merged': project['pulls_merged']})
main()
