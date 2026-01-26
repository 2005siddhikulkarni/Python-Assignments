def AddList(Num):
    lst = []
    print("Enter the numbers: ")
    for i in range(1,Num+1):
        Values = int(input())
        lst.append(Values)

    Total = 0
    for i in lst:
        Total += i
    return Total

def main():
    print("Enter the number: ")
    No = int(input())

    Result = AddList(No)
    print("Sum is: ",Result)


if __name__ == "__main__":
    main()