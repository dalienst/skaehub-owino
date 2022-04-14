# READ A GIVEN CSV FILE AS A DICTIONARY
# WE USE csv.DictReader() TO READ A CSV FILE AS A DICTIONARY
# TEST DATA IS NAMES.CSV
import csv
with open("names.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(dict(row))