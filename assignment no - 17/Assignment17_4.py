def AddFactors(No):
    Ans = 0
    for i in range(1,No):
        if No % i == 0:
            Ans += i
    return Ans 

def main():
    print("Enter the number: ")
    Value1 = int(input())
 
    Result = AddFactors(Value1)
    print("Addition of factors is: ",Result)

if __name__ == "__main__":
    main()