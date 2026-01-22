from functools import reduce

Addition = lambda No1,No2 : No1 + No2 

def main():
    lst = list(map(int, input("Enter numbers: ").split()))

    Result = reduce(Addition, lst)
    print("Sum is: ",Result)


if __name__ == "__main__":
    main()