
Square = lambda Nos : Nos * Nos

def main():
    lst = []

    print("Enter the number: ")
    No = int(input())

    print("Enter the numbers: ")
    for i in range(1,No+1):
        Values = int(input())
        lst.append(Values)

    Result = list(map(Square, lst))
    print(Result)

if __name__ == "__main__":
    main()
