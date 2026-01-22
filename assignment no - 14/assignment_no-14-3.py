
MaxNo = lambda No1,No2 : No1 if No1 > No2 else No2

def main():
    Value1 = print("Enter the first number: ")
    Value1 = int(input())

    Value2 = print("Enter the second number: ")
    Value2= int(input())

    print("Maximum number is: ",MaxNo(Value1, Value2))

if __name__ == "__main__":
    main()