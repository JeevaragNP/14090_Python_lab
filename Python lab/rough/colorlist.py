c=input("Enter the colours of list 1:").split(",")
print("List 1:",c)
d=input("Enter the colours of list 2:").split(",")
print("List 1:",c)
e=set(c)
f=set(d)
sc=e.difference(f)
lc=list(sc)
print("Difference is:",lc)


