import csv

with open('mpg.csv') as csvFile:
    mpg = list(csv.DictReader(csvFile))

print(mpg[0])
