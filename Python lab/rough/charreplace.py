st1 = str(input("Enter the string:"))
a = st1[0]
for i in st1:
    if i==a:
        st1 = st1.replace(i,"$")
        st1 = a + st1[1:]
print(st1)