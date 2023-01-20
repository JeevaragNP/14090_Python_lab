# Write a python program to write a python dictionary to a CSV file.
# After writing the CSV file read and display the content.

import csv

# Data to be inserted
data = [{'Name': 'Jeevan', 'Age': '21', 'Country': 'India'},
        {'Name': 'Ashiq', 'Age': '22', 'Country': 'India'},
        {'Name': 'Kiran', 'Age': '23', 'Country':'India'}]

# Write to CSV file
with open('people.csv', 'w') as csvfile:
    headernames = ['Name', 'Age', 'Country']
    csvwriter = csv.DictWriter(csvfile, fieldnames=headernames)
    csvwriter.writeheader()
    for row in data:
        csvwriter.writerow(row)

# read from CSV file and print contents
with open('people.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
