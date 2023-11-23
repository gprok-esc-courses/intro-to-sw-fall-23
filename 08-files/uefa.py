# Find how many times each team played
# Find how many times each country was represented

import csv 

file = open("uefa.csv", encoding="utf8")
reader = csv.DictReader(file)

teams = {}
for row in reader:
    if row['code'] in teams: # already found
        teams[row['code']] += 1
    else: # found for the first time
        teams[row['code']] = 1

for key in teams:
    print(key, teams[key])