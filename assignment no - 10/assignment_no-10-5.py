def Odd(Value1):
    for i in range(1,Value1+1,2):
        print(i)


def main():
    No1 = print("Enter the number: ")
    No1 = int(input())

    Odd(No1)

if __name__ == "__main__":
    main()