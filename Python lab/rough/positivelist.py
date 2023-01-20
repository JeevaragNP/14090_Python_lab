n = int(input("Enter the limit."))
li = []
i = 0
print("Enter the elements: ")
for i in range(n):
    ele = int(input())
    if ele > 0:
        li.append(ele)
print("Positive list: ", li)