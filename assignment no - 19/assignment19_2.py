MultOfTwo = lambda No1, No2 : No1 * No2


def main():
    Value1 = print("Enter first number: ")
    Value1 = int(input())

    Value2 = print("Enter second number: ")
    Value2 = int(input())


    Result = MultOfTwo(Value1, Value2)
    print("Multiplication is: ",Result)

if __name__ == "__main__":
    main()