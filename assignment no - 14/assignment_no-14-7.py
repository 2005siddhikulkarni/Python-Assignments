
DivisibleNo = lambda No: True if No % 5 == 0 else False

def main():
    Value = print("Enter the first number: ")
    Value = int(input())
    
    print("Divisible by 5: ",DivisibleNo(Value))

if __name__ == "__main__":
    main()