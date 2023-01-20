a = "hai how are you hai"
b = a.split()
count = 0
word = str(input("Enter the string:"))
for i in b:
    if i == word:
        count = count+1
print(count)
