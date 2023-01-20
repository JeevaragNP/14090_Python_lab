i=1
sum=0
sum2=0
n=int(input("Enter the limit"))
while(i<=n):
    if i%2==0:
        sum=sum+i
    else:
        sum2=sum2+i
    i=i+1
print("Even sum:",sum)
print("Odd sum:",sum2)