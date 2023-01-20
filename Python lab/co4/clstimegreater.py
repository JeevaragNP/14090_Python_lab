class Time:
    def __init__(self, hr, mn, sc):
        self.__hour = hr
        self.__minute = mn
        self.__second = sc

    def __gt__(self, other):
        if self.__hour > other.__hour:
            return True
        elif self.__hour == other.__hour:
            if self.__minute > other.__minute:
                return True
            elif self.__minute == other.__minute:
                if self.__second > other.__second:
                    return True
                elif self.__second == other.__second:
                    print("Time is equal")
                else:
                    return False
            else:
                return False
        else:
            return False



h = int(input("Enter the hour:"))
m = int(input("Enter the minute:"))
s = int(input("Enter the seconds:"))
h1 = int(input("Enter the hour:"))
m1 = int(input("Enter the minute:"))
s1 = int(input("Enter the seconds:"))

t1 = Time(h, m, s)
t2 = Time(h1, m1, s1)
if t1 > t2:
    print("t1 is greater than t2")
else:
    print("t2 is greater than t1")
