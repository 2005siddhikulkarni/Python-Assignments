from functools import reduce

MinNo = lambda No1,No2 : No1 if No1 < No2 else No2

def main():
    lst = []

    print("Enter the number: ")
    No = int(input())

    print("Enter the numbers: ")
    for i in range(1, No + 1):
        Values = int(input())
        lst.append(Values)
        
    Result = reduce(MinNo, lst)
    print("Minimum number is: ",Result)


if __name__ == "__main__":
    main()
