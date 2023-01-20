n=int(input("Enter the number:"))
flag=0
i=2
while i <= n/2:
    if n%i == 0:
        flag=1
        break
    i=i+1
if flag == 0:
    print("The number is prime.")
else:
    print("The number is not prime.")