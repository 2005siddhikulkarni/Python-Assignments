from functools import reduce

Multiply = lambda No1,No2 : No1 * No2 

def main():
    lst = list(map(int, input("Enter numbers: ").split()))

    Result = reduce(Multiply, lst)
    print("Multiplication is: ",Result)


if __name__ == "__main__":
    main()