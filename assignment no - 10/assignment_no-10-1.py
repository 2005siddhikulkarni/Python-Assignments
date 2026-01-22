def Multiplication(Value1):
    for i in range(1,11):
        Result = Value1 * i
        print(Result)


def main():
    No1 = print("enter the number: ")
    No1 = int(input())

    Multiplication(No1)

if __name__ == "__main__":
    main()