def ChkMin(Num):
    lst = []
    print("Enter the numbers: ")
    for i in range(1,Num+1):
        Values = int(input())
        lst.append(Values)

    Min = lst[0]
    for i in range(1,len(lst)+1):
        if i < Min:
            Min = i
    return Min

def main():
    print("Enter the number: ")
    No = int(input())

    Result = ChkMin(No)
    print("Minimum number is: ",Result)


if __name__ == "__main__":
    main()