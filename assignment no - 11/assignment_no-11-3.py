
def SumOfDigits(Value1):
    Sum = 0
    for i in range(0,len(Value1)+1):
        Sum += i
    
    return Sum


def main():
    No1 = print("enter the number: ")
    No1 = input()

    Result = SumOfDigits(No1)
    print("Sum is: ",Result)

if __name__ == "__main__":
    main()