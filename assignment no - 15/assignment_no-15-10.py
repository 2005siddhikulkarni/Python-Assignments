
from functools import reduce

CntEvenNo = lambda No: No % 2 == 0

def main():
    lst = []

    print("Enter the number: ")
    No = int(input())

    print("Enter the numbers: ")
    for i in range(No):
        Values = int(input())
        lst.append(Values)

    Result = list(filter(CntEvenNo, lst))
    print("Count of even numbers is:", len(Result))

if __name__ == "__main__":
    main()
