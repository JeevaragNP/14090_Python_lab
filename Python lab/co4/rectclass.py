class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width

    def peri(self):
        return (self.length + self.width) * 2


l1 = float(input("Enter the length of 1st rectangle:"))
b1 = float(input("Enter the breadth of 1st rectangle:"))
l2 = float(input("Enter the length of 2nd rectangle:"))
b2 = float(input("Enter the breadth of 2nd rectangle:"))
rect1 = Rectangle(l1, b1)
rect2 = Rectangle(l2, b2)
print("Area of rectangle 1 is {} and perimeter is {}:".format(rect1.area(), rect1.peri()))
print("Area of rectangle 2 is {} and perimeter is {}:".format(rect2.area(), rect2.peri()))
print(rect1.area() > rect2.area())
