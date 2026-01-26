
Divisible = lambda No : No % 3 == 0 and No % 5 == 0

def main():
    lst = []

    print("Enter the number: ")
    No = int(input())

    print("Enter the numbers: ")
    for i in range(1, No + 1):
        Values = int(input())
        lst.append(Values)

    Result = list(map(Divisible, lst))
    print(Result)


if __name__ == "__main__":
    main()
