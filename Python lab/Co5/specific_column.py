import csv

# specify the column indices that you want to read
columns_to_read = [0,2]

# open the CSV file and read the contents
with open('demo.csv', 'r') as file:
    clmn_reader = csv.reader(file)

    # iterate over the rows of the CSV
    for row in clmn_reader:
        # print the contents of the specified columns
        print([row[i] for i in columns_to_read])