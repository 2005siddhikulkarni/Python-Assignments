
def MathOperation(Value1, Value2):
    Addition = Value1 + Value2
    print("Addition is: ",Addition)

    Subtraction = Value1 - Value2
    print("Subtraction is: ",Subtraction)

    Multiplication = Value1 * Value2
    print("Multiplication is: ",Multiplication)

    Division = Value1 / Value2
    print("Division is: ",Division)

def main():
    No1 = print("Enter the first number: ")
    No1 = int(input())

    No2 = print("Enter the second number: ")
    No2 = int(input())

    MathOperation(No1, No2)

if __name__ == "__main__":
    main()