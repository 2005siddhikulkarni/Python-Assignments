from functools import reduce

MaxNo = lambda No1,No2 : No1 if No1 > No2 else No2

def main():
    lst = list(map(int, input("Enter numbers: ").split()))

    Result = reduce(MaxNo, lst)
    print("Maximum number is: ",Result)


if __name__ == "__main__":
    main()