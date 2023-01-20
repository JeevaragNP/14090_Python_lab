# program to copy odd lines of one file to another.
# opening files for reading and writing data.

input_file = open('Data.txt')
output_file = open('WriteData.txt', 'w')

# copying/reading from read file to copy_data
copy_data = input_file.readlines()
print("\nActual file content is :")
print([x.strip() for x in copy_data])

for i in range(0, len(copy_data)):
    if i % 2 == 0:
        output_file.write(copy_data[i])
    else:
        pass

# Closing file after writing
output_file.close()

# opening write file in read mode and printing values
output_file = open('WriteData.txt', 'r')
print("\nOdd lines are:")
print(output_file.read())


# closing files
input_file.close()
output_file.close()
