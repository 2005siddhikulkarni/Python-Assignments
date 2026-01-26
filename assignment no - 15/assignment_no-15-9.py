from functools import reduce

Multiply = lambda No1,No2 : No1 * No2 

def main():
    lst = []

    print("Enter the number: ")
    No = int(input())

    print("Enter the numbers: ")
    for i in range(1, No + 1):
        Values = int(input())
        lst.append(Values)

    Result = reduce(Multiply, lst)
    print("Multiplication is: ",Result)


if __name__ == "__main__":
    main()
