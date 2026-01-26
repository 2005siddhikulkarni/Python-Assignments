def Print(Num):
    for i in range(1,Num+1):
        print("*",end = " ")

def main():
    print("Enter the number: ")
    Value = int(input())

    Print(Value)

if __name__ == "__main__":
    main()