dic = { "Germany":"BMW", "Italy":"Lamborghini","Japan":"Nissan" }
l = list(dic.items())
l.sort()
print("Sort in ascending order:",l)
l1 = list(dic.items())
l1.sort(reverse=True)
print("Sort in descending order is:",l1)