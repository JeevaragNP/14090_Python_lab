import csv

# Open the csv file
with open('datas1.csv', 'r') as file:
    # Create a CSV reader
    reader = csv.reader(file)

    # iterate over the rows of the CSV file
    for row in reader:
        # print the row as a list of strings
        print(row)