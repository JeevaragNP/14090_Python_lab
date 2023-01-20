l = int(input("Enter the length of rectangle:"))
b = int(input("Enter the breadth:"))
arec = lambda l, b : l*b
print("Area of rectangle =",arec(l,b))

s = int(input("Enter the side of square:"))
arsq = lambda s : s*s
print("Area of square =",arsq(s))

l1 = int(input("Enter the length of triangle:"))
h = int(input("Enter the height:"))
artr = lambda l1, h : 1/2*l*b
print("Area of triangle=",artr(l1,h))