
EvenNo = lambda No: No % 2 == 0

def main():
    lst = list(map(int, input("Enter numbers: ").split()))

    Result = list(filter(EvenNo, lst))
    print("Even numbers are: ",Result)


if __name__ == "__main__":
    main()