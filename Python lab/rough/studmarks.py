name =input("Enter the name of the student: ")
m1 = int(input("Total marks in Python: "))
m2 = int(input("Total marks in C: "))
m3 = int(input("Total marks in Java: "))
m4 = int(input("Total marks in C++: "))
m5 = int(input("Total marks in HTML: "))
total = m1+m2+m3+m4+m5
per = total/500 * 100
print("Total marks is",total)
print("Total percentage is",per,"%")
