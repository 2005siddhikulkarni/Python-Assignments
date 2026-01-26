def PosOrNeg(Num):
    if Num > 0 :
        print("Positive Number")

    elif Num < 0 :
        print("Negative Number")

    else :
        print("Zero")

def main():
    print("Enter the number: ")
    Value = int(input())

    PosOrNeg(Value)

if __name__ == "__main__":
    main()