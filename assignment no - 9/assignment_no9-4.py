
def Cube_No(Value1):
    Ans = Value1 ** 3
    return Ans

def main():
    No1 = print("Enter the number: ")
    No1 = int(input())

    Result = Cube_No(No1)
    print("The cube of number is: ",Result)


if __name__ == "__main__":
    main()