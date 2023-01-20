n1 = 2022
n2 = int(input("Enter the limit year:"))
print("The leap years are:")
for i in range(n1,n2):
    if i % 400 == 0 or i % 100 != 0 and i % 4 == 0:
        print(i, end=" ")


