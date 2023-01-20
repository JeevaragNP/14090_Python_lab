'''n=int(input("Enter the limit:"))
l1=[]
print("Enter the elements:")
for i in range(n):
    val=eval(input())
    l1.append(val)
print(l1)
l = []
while True:
    val = int(input("Enter the elements:"))
    l.append(val)
    ch = input("Enter s to quit")
    if ch == 's':
        break
print(l)'''
i=0
for i in range(6,0,-1):
    j=0
    for j in range(i+1):
        print("*", end="")
    print("\n")

