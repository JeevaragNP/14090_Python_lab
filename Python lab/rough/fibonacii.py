l=int(input("Enter the limit"))
a,b=0,1
i=0
print("Fiboncaii series:")
while i<l:
    print(a)
    c=a+b
    a=b
    b=c
    i=i+1
