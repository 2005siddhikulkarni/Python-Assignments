def NumberCheck(Value1):
    if Value1 % 3 == 0 and Value1 % 5 == 0 :
        print("the number is divisible by 3 and 5")

    else :
        print("the number is not divisible by 3 and 5")



def main():
    No1 = print("Enter the number: ")
    No1 = int(input())

    NumberCheck(No1)


if __name__ == "__main__":
    main()