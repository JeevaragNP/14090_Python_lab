st = str(input("Enter a string:"))
if st[-3:] == 'ing':
    st = st.replace("ing","ly")
else :
    st = st + "ing"
print(st)