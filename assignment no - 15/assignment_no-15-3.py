
OddNo = lambda No: No % 2 != 0

def main():
    lst = list(map(int, input("Enter numbers: ").split()))

    Result = list(filter(OddNo, lst))
    print("Odd numbers are: ",Result)


if __name__ == "__main__":
    main()