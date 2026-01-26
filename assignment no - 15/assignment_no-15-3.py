
OddNo = lambda No: No % 2 != 0

def main():
    lst = []

    print("Enter the number: ")
    No = int(input())

    print("Enter the numbers: ")
    for i in range(1,No+1):
        Values = int(input())
        lst.append(Values)

    Result = list(filter(OddNo, lst))
    print("Odd numbers are: ",Result)


if __name__ == "__main__":
    main()
