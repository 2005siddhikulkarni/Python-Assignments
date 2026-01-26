import MarvellousNum

def AddPrime(Num):
    lst = []
    print("Enter the numbers: ")
    for i in range(1,Num+1):
        Values = int(input())
        lst.append(Values)

    NewLst = []
    for i in lst:
        if MarvellousNum.ChkPrime(i):
            NewLst.append(i)

    Total = 0
    for i in NewLst:
        Total += i
    return Total
    

def main():
    print("Enter the number: ")
    No = int(input())

    Result = AddPrime(No)
    print("Addition of prime numbers is: ",Result)


if __name__ == "__main__":
    main()