st=int(input("Enter the starting limit:"))
en=int(input("Enter the ending limit:"))
print("Armstrong numbers are:")
i=st;
while i<=en:
    temp=i
    sum=0
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if(i==sum):
        print(i)
    i = i+1