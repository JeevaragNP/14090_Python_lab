'''a = int(input("Enter the first number:"))
b= int(input("Enter the second number:"))
sum = lambda a,b : a+b
print("Sum =",sum(a,b))'''

'''def add(a,b):
    c = a+b
    print("sum = ",c)
add(20,55)'''

a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
def add(a,b):
    sum=a+b
    return sum
result=add(a,b)
print("sum = ",result)