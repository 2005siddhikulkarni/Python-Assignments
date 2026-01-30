class Circle():
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        print("Enter the radius: ")
        self.Radius = float(input())

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("The value of radius is: ",self.Radius)
        print("Area of the circle is: ",self.Area)
        print("Circumference of the circle is: ",self.Circumference)


obj1 = Circle()
obj2 = Circle()
obj3 = Circle()
obj4 = Circle()

print("For obj1")
obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()

print("For obj2")
obj2.Accept()
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()

print("For obj3")
obj3.Accept()
obj3.CalculateArea()
obj3.CalculateCircumference()
obj3.Display()

print("For obj4")
obj4.Accept()
obj4.CalculateArea()
obj4.CalculateCircumference()
obj4.Display()


