

def Sum(Value1):
    Result = 0
    for i in range(1,Value1+1,):
        Result += i
    return Result


def main():
    No1 = print("Enter the number: ")
    No1 = int(input())

    Ans = Sum(No1)
    print("Sum of first N natural number is: ",Ans)

if __name__ == "__main__":
    main()