import Arithmetic

def main():
    print("Enter first number: ")
    Value1 = int(input())

    print("Enter second number: ")
    Value2 = int(input())

    print("Addition is: ",Arithmetic.Add(Value1, Value2))
    print("Subtraction is: ",Arithmetic.Sub(Value1, Value2))
    print("Multiplication is: ",Arithmetic.Mult(Value1, Value2))
    print("Division is: ",Arithmetic.Div(Value1, Value2))


if __name__ == "__main__":
    main()