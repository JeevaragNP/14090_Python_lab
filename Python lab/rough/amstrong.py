num=int(input("Enter the number:"))
i=num
sum=0
while(num>0):
    rem=num%10
    sum=sum+rem**3
    num=num//10
if i==sum:
    print("The number is Amstrong")
else:
    print("The number is not Amstrong")
