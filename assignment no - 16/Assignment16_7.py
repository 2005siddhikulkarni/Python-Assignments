def ChkDivisible(Num):
    if Num % 5 == 0 :
        return True
    
    else :
        return False

def main():
    print("Enter the number: ")
    Value = int(input())

    Result = ChkDivisible(Value)
    print(Result)

if __name__ == "__main__":
    main()