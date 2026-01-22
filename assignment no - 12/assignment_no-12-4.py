def PrintingNumbers(No1):
    for i in range(1,No1+1):
        print(i,end=" ")

def main():
    Value1 = print("Enter the number: ")
    Value1 = int(input())

    PrintingNumbers(Value1)

if __name__ == "__main__":
    main()