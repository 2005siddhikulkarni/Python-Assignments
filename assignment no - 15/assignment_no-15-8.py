
Divisible = lambda No : No % 3 == 0 and No % 5 == 0

def main():
    lst = list(map(int, input("Enter numbers: ").split()))

    Result = list(map(Divisible, lst))
    print(Result)


if __name__ == "__main__":
    main()