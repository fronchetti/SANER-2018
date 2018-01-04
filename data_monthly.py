try:
    import os
    import json
    import csv
    import numpy
    from datetime import datetime
except ImportError as error:
    raise ImportError(error)

dataset = './Dataset/'
folders = os.listdir(dataset)

def project_monthly_contributions(file):
	contributions = {}
	for line in file:
		date = datetime.strptime(line.strip(), '%Y-%m-%d').date().replace(day = 15)		
		if date in contributions:
			contributions[date] = contributions[date] + 1
		else:
			contributions[date] = 1
	return contributions
		
def main():
    projects_contributions = {}
    for project in folders:
        folder = dataset + project
        if os.path.isfile(folder + '/commits.csv'):
			contributions_file = open(folder + '/commits.csv', 'r')
			contributions = project_monthly_contributions(contributions_file)
			
			for date in contributions:
				if date in projects_contributions:
					projects_contributions[date] = projects_contributions[date] + [contributions[date]]
				else:
					projects_contributions[date] = [contributions[date]]
        else:
			print(project + " does not contain a contributions file.")

	with open('monthly_contributions.csv', 'w') as csv_file:
		fieldnames = ['Date', 'Amount', 'Mean', 'Median']
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		writer.writeheader()
		
		for date in projects_contributions:
			amount = sum(projects_contributions[date])
			mean = numpy.mean(projects_contributions[date])
			median = numpy.median(projects_contributions[date])
			writer.writerow({'Date': date, 'Amount': amount, 'Mean': mean, 'Median': median})
main()
