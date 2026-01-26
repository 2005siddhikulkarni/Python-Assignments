import functools 

FData = lambda A: A >= 70 and A <= 90 
MData = lambda A: A + 10
RData = lambda A,B: A * B


def main():
    lst = []

    print("Enter the number: ")
    No = int(input())

    print("Enter the elements: ")
    for i in range(No):
        Values = int(input())
        lst.append(Values)

    Result1 = list(filter(FData, lst))
    print("list after filter is: ",Result1)

    Result2 = list(map(MData, Result1))
    print("list after map is: ",Result2)

    Result3 = functools.reduce(RData, Result2)
    print("list after filter is: ",Result3)
   

if __name__ == "__main__":
    main()