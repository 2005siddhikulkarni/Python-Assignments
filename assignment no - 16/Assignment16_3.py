def Add(No1, No2):
    Ans = No1 + No2
    return Ans

def main():
    print("Enter first number: ")
    Value1 = int(input())

    print("Enter second number: ")
    Value2 = int(input())

    Result = Add(Value1, Value2)
    print(Result)

if __name__ == "__main__":
    main()