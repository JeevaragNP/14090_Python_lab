st = str(input("Enter a string"))
st2 = set(st)
for i in st2:
    c = 0
    for j in (len(st)):
        if i==st2[j]:
            c = c+1
    print(i,":",c)
