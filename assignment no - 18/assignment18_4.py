def ChkFreq(Num):
    lst = []

    print("Enter the numbers: ")
    for i in range(1,Num+1):
        Values = int(input())
        lst.append(Values)

    Value1 = print("Enter the number to check frequency: ")
    Value1 = int(input())

    Cnt = 0
    for i in lst:
        if i == Value1:
            Cnt += 1
    return Cnt

def main():
    print("Enter the number: ")
    No = int(input())

    Result = ChkFreq(No)
    print("Frequency of number is: ",Result)


if __name__ == "__main__":
    main()