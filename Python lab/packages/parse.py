import csv
csv_string = """1,2,3,4,5,6,7,8,9"""
print("original string:")
print(csv_string)
lines = csv_string.splitlines()
print("list of csv formatted strings:")
print(lines)
readers = csv.reader(lines)
parsed_csv = list(readers)
print("\nList representation of csv file:")
print(parsed_csv)