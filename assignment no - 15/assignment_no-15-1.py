
Square = lambda Nos : Nos * Nos

def main():
    lst = list(map(int, input("Enter numbers: ").split()))

    Result = list(map(Square, lst))
    print(Result)


if __name__ == "__main__":
    main()