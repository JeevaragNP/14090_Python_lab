l1=int(input("Enter the size of list 1 : "))
l2=[]
for i in range (0,l1):
    a=int(input("Enter Number : "))
    l2.append(a)
print("\nList 1 is ;", l2)

l3=int(input("\nEnter the size of list 2 : "))
l4=[]
for i in range (0,l3):
    b=int(input("Enter Number : "))
    l4.append(b)
print("\nList 2 is : ", l4)

if (len(l2)==len(l4)):
    print("\nThe size of both list are equal")
else:
    print("\nThe size of both list are not equal")

if (sum(l2)==sum(l4)):
    print("\nSum of both list is equal")
else:
    print("\nSum of both list are not equal")

print("\nCommon elements in both list are : ")

for i in l2:
    for j in l4:
        if(i==j):
            print(i)
