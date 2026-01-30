class Arithmetic():
    PI = 3.14

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
       
    def Accept(self):
        print("Enter the first Value: ")
        self.Value1 = int(input())

        print("Enter the second Value: ")
        self.Value2 = int(input())


    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        if self.Value2 == 0:
           return "Division is not allowed"

        else:
            return self.Value1 / self.Value2
        
    
obj1 =Arithmetic()
obj2 = Arithmetic()

print("For obj1")

obj1.Accept()

obj1.Addition()
print("Addition is: ",obj1.Addition())

obj1.Subtraction()
print("Subtraction is: ",obj1.Subtraction())

obj1.Multiplication()
print("Multiplication is: ",obj1.Multiplication())

obj1.Division()
print("Division is: ",obj1.Division())

print("For obj2")

obj2.Accept()

obj2.Addition()
print("Addition is: ",obj2.Addition())

obj2.Subtraction()
print("Subtraction is: ",obj2.Subtraction())

obj2.Multiplication()
print("Multiplication is: ",obj2.Multiplication())

obj2.Division()
print("Division is: ",obj2.Division())