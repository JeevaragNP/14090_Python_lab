num=int(input("Enter the number:"))
rev=0
num1=num
for i in range(num):
    if num != 0:
        r=num%10
        num=num//10
        rev=rev*10+r
    else:
        break
print("The reversed number is:",rev)