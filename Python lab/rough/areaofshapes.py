l = int(input("Enter the length:"))
b = int(input("Enter the breadth:"))
h = int(input("Enter the height:"))

sar = lambda l : l*l
print("Area of Square = ",sar(l))

rar = lambda l,b :l*b
print("Area of Rectangle = ",rar(l,b))

tar = lambda b,h : (b*h)/2
print("Area of Triangle = ",tar(b,h))
