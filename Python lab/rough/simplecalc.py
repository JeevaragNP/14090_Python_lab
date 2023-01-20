c=int(input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\nEnter your choice:"))
a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number:"))
if c==1:
    print("Sum = ",a+b)
elif c==2:
    print("Difference = ",a-b)
elif c==3:
    print("Product = ",a*b)
elif c==4:
    print("Dividend = ",a/b)
else:
    print("Invalid choice.")