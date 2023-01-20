l=int(input("Enter the limit"))
a,b=0,1
print("Fiboncaii series:")
for i in range(0,l):
    print(a, end=" ")
    c=a+b
    a=b
    b=c
