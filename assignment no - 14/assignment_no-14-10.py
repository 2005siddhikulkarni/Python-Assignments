
MaxNo = lambda No1,No2,No3 : No1 if( No1 > No2 and No1 > No3) else No2 if (No2 > No1 and No2 > No3) else No3

def main():
    Value1 = print("Enter the first number: ")
    Value1 = int(input())

    Value2 = print("Enter the second number: ")
    Value2= int(input())

    Value3 = print("Enter the third number: ")
    Value3 = int(input())


    print("Maximum number is: ",MaxNo(Value1, Value2, Value3))

if __name__ == "__main__":
    main()