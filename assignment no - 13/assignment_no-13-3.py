def PerfectNoOrNot(Value1):
    Sum = 0

    for i in range(1,Value1):
        if Value1 % i == 0 :
            Sum += i
           
    if Value1 == Sum :
        Result = print("Perfect number")

    else:
        Result = print("Not a perfect number")

    return Result

def main():
    No1 = print("Enter the number: ")
    No1 = int(input())

    PerfectNoOrNot(No1)

if __name__ == "__main__":
    main()