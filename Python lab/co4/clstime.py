class Time:
    def __init__(self,hr,mn,sc):
        self.__hour = hr
        self.__minute = mn
        self.__second = sc

    def __add__(self,other):
        return 'time is: ' + str(self.__hour + other.__hour) + ':' +str(self.__minute + other.__minute) + ':' + str(self.__second + other.__second)


h = int(input("Enter the hour:"))
m = int(input("Enter the minute:"))
s = int(input("Enter the seconds:"))
h1 = int(input("Enter the hour:"))
m1 = int(input("Enter the minute:"))
s1 = int(input("Enter the seconds:"))

t1 = Time(h, m, s)
t2 = Time(h1, m1, s1)
print(t1 + t2)

