# program to read file content and store it into a list.
# using readlines()
open_file = open("test.txt", 'r')
file_lines = open_file.readlines()

# print without strip
print("File contents with newline character: ")
print(file_lines)


# print with strip
print("\nFile content without newline character: ")
file_lines = [x.strip() for x in file_lines]
print([x.strip() for x in file_lines])
open_file.close()
