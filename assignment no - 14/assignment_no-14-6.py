
OddNo = lambda No: True if No % 2 != 0 else False

def main():
    Value = print("Enter the first number: ")
    Value = int(input())
    
    print("Odd number: ",OddNo(Value))

if __name__ == "__main__":
    main()