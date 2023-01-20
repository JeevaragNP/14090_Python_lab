n = int(input("Enter the number:"))
def facto(a):
    fac = 1
    for i in range(2,a+1):
        fac = fac*i
    return fac
print("Factorial = ", facto(n))