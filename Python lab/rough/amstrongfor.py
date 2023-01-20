num=int(input("Enter the number:"))
i=num
sum=0
for j in range(0,num):
    rem=num%10
    sum=sum+rem**3
    num=num//10
if i==sum:
    print("The number is Armstrong")
else:
    print("The number is not Armstrong")