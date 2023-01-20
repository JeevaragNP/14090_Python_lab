n = int(input("Enter the limit:"))
li= []
count = 0
for i in range (0,n):
    fn = input("Enter the first name:")
    li.append(fn)
print(li)
for i in li:
    for j in i:
        if j=='a':
            count = count +1
print("The occurance of 'a' is :", count)