
EvenNo = lambda No: No % 2 == 0

def main():
    lst = []

    print("Enter the number: ")
    No = int(input())

    print("Enter the numbers: ")
    for i in range(1,No+1):
        Values = int(input())
        lst.append(Values)
        
    Result = list(filter(EvenNo, lst))
    print("Even numbers are: ",Result)


if __name__ == "__main__":
    main()
