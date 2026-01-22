def PrintingReverseNumbers(No1):
    for i in range(No1,0,-1):
        print(i,end=" ")

def main():
    Value1 = print("Enter the number: ")
    Value1 = int(input())

    PrintingReverseNumbers(Value1)

if __name__ == "__main__":
    main()