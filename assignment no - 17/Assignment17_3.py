def Fact(No):
    Ans = 1
    for i in range(No,0,-1):
        Ans *= i
    return Ans  

def main():
    print("Enter the number: ")
    Value1 = int(input())
 
    Result = Fact(Value1)
    print("Factorial is: ",Result)

if __name__ == "__main__":
    main()