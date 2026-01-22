
def ReverseNO(Value1):
    Rev = 0
    while Value1 > 0 :
        Digit = Value1 % 10
        Rev = Rev * 10 + Digit
        Value1 = Value1 // 10
    return Rev

def main():
    No1 = print("enter the number: ")
    No1 = int(input())

    Result = ReverseNO(No1)
    print("Reverse number is: ",Result)

if __name__ == "__main__":
    main()