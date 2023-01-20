sen = input("Enter a string:").split()
l = (set(sen))
for i in l:
    print(i,":",sen.count(i))