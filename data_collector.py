# -*- coding: utf-8 -*-
# Author:  Felipe Fronchetti
# Doubts? fronchettiemail@gmail.com
# This code is responsible for collect data of each project used in our
# research.

try:
    import multiprocessing
    from functools import partial
    import Crawler.crawler as GitCrawler
    import Crawler.repository as GitRepository
    import json
    import csv
    import subprocess
    import os
except ImportError as error:
    raise ImportError(error)


class Repository():

    def __init__(self, url, folder, collector):
        self.collector = collector
        self.folder = folder
        self.url = url

        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

    def clone(self):
        repository_folder = self.folder + '/repository'

        if not os.path.exists(repository_folder):

            about_file = self.folder + '/about.json'
            if os.path.isfile(about_file):
               about = json.load(open(self.folder + '/about.json', 'r'))           
               if about:
                  self.url = about['clone_url']

            try:
                os.makedirs(repository_folder)
                subprocess.call(['git', 'clone', self.url, repository_folder])
            except:
                print("Erro ao clonar:" + str(self.url))

    def loc(self):
        loc_file = self.folder + '/loc.json'

        if not os.path.isfile(loc_file):
            subprocess.call(['cloc', '--json', '--out=' + loc_filerand, self.folder + '/repository'])

    def about(self):
        about_file = self.folder + '/about.json'

        if not os.path.isfile(about_file):
            about = self.collector.get()

            with open(about_file, 'w') as file:
                json.dump(about, file, indent = 4)
    
    def stars(self):
        stars_file = self.folder + '/stars.json'

        if not os.path.isfile(stars_file):
            stars = self.collector.stars()

            with open(stars_file, 'w') as file:
                json.dump(stars, file, indent = 4)

    def forks(self):
        forks_file = self.folder + '/forks.json'

        if not os.path.isfile(forks_file):
            forks = self.collector.forks()

            with open(forks_file, 'w') as file:
                json.dump(forks, file, indent = 4)

    def pull_requests(self):
        pulls_file = self.folder + '/pulls.json'

        if not os.path.isfile(pulls_file):
            pull_requests = self.collector.pull_requests(state='all')
    
            with open(pulls_file, 'w') as file:
                json.dump(pull_requests, file, indent = 4)

    def languages(self):
        languages_file = self.folder + '/languages.json'

        if not os.path.isfile(languages_file):
            languages = self.collector.languages()
                
            with open(languages_file, 'w') as file:
                json.dump(languages, file, indent = 4)

    def commits(self):
        commits_file = self.folder + '/commits.csv'
        repository_folder = self.folder + '/repository'

        if os.path.isfile(commits_file):
            if os.path.exists(repository_folder):
                subprocess.call(['sh', 'Crawler/commits.sh', repository_folder])
            else:
                print("Repository has not been cloned yet.")

    def newcomers(self):
        newcomers_file = self.folder + '/newcomers.csv'
        repository_folder = self.folder + '/repository'

        if not os.path.isfile(newcomers_file):
            if os.path.exists(repository_folder):
                subprocess.call(['sh', 'Crawler/newcomers.sh', repository_folder])
            else:
                print("Repository has not been cloned yet.")

def repositories_in_parallel(project):
    organization, name, url, folder = project['organization'], project['name'], project['url'], project['folder']

    collector = GitRepository.Repository(organization, name, crawler)
    R = Repository(url, folder, collector)
    # R.about()  # Creates a file with general data about the project
    # R.clone()  # Clone the repository
    # R.newcomers()  # Creates a file with all newcomers in the project
    # R.pull_requests()  # Creates a file with all the pull requests submmited to the repository
    R.commits()  # Creates a file with all the contributions submmited to the repository
    # R.stars()  # Creates a file with all stars evaluated in the repository (Include evaluation date)
    # R.forks()  # Creates a file with all the copies created from the repository
    # R.languages() # Creates a file with all languages used in the repository
    # R.loc() # Creates a file describing LoC used in the repository

if __name__ == '__main__':
    dataset_folder = 'Dataset/'
    api_client_id = '#' # Please, specify your own client id
    api_client_secret = '#' # Please, specify your own client secret
    crawler = GitCrawler.Crawler(api_client_id, api_client_secret)
    repositories = []

    with open('responses.csv', 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            column = row['8. Is your R package maintained in a public repository (e.g., GitHub)? If so, what is the URL?'].strip()

            if '.git' in column:
                column = column.replace('.git', '')

            if 'www.' in column:
                column = column.replace('www.', '')

            if 'http://github.com/' in column:
                column = column.replace('http://github.com/', 'https://github.com/')

            if 'https://github.com/' in column:
                info = column.replace('https://github.com/', '')
                info = info.split('/')

                if len(info) > 1:
                    project = {'name': info[1], 'organization': info[0], 'url': column, 'folder': dataset_folder + info[1]}
                    repositories.append(project)

    parallel = multiprocessing.Pool(processes=1) # Define number of processes
    parallel.map(partial(repositories_in_parallel), repositories)
