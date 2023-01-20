a=input("Enter the 1st list elements separated with commas: ")
b=input("Enter the 2st list elements separated with commas: ")
c=a.split(",")
d=b.split(",")
e=set(c)
f=set(d)
g=e.difference(f)
h=list(g)
print("The difference is: ",h)



