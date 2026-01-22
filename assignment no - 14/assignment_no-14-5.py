
EvenNo = lambda No: True if No % 2 == 0 else False

def main():
    Value = print("Enter the first number: ")
    Value = int(input())
    
    print("Even number: ",EvenNo(Value))

if __name__ == "__main__":
    main()