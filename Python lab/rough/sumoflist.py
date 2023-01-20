n1 = int(input("Enter the limit of 1st list:"))
l1 = []
print("Enter the list elements:")
for i in range(n1):
    a = int(input())
    l1.append(a)
print("List 1:", l1)
sum1 = 0
c = len(l1)
for i in range(len(l1)):
    sum1 = sum1 + l1[i]
print("Sum of list =", sum1)
