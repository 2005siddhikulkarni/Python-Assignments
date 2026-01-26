def ChkMax(Num):
    lst = []
    print("Enter the numbers: ")
    for i in range(1,Num+1):
        Values = int(input())
        lst.append(Values)

    Max = lst[0]
    for i in range(1,len(lst)+1):
        if i > Max:
            Max = i
    return Max

def main():
    print("Enter the number: ")
    No = int(input())

    Result = ChkMax(No)
    print("Maximum number is: ",Result)


if __name__ == "__main__":
    main()