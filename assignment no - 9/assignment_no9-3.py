
def SquareNo(Value1):
    Ans = Value1 * Value1
    return Ans



def main():
    No1 = print("Enter the number: ")
    No1 = int(input())

    Result = SquareNo(No1)
    print("Square of the number is: ",Result)

if __name__ == "__main__":
    main()