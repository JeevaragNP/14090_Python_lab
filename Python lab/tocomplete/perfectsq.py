n1 = int(input("Enter the lower limit:"))
n2 = int(input("Enter the upper limit:"))
while n1<n2:
    for i in range (n1):
        if (i*i==n1) and (i%2==0):
            n1=n1+1
    print(i)



