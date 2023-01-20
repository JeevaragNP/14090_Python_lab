n=int(input("Enter the limit."))
i=1
while i<=n:
    j=n
    while j>= i:
        print("*",end=" ")
        j-=1
    print(" ")
    i+=1