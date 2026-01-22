

def Fact(Value1):
    Ans = 1
    for i in range(Value1,0,-1):
        Ans *= i
    return Ans

def main():
    No1 = print("Enter the number: ")
    No1 = int(input())

    Result = Fact(No1)
    print("Factorial of",No1,"is: ",Result)

if __name__ == "__main__":
    main()