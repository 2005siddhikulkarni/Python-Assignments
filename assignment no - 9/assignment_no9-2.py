
def ChkGreater(Value1, Value2):
    if Value1 > Value2 :
        print(Value1,"is greater")

    else :
        print(Value2,"is greater")


def main():
    No1 = print("Enter first number: ")
    No1 = int(input())

    No2 = print("Enter second number: ")
    No2 = int(input())

    ChkGreater(No1,No2)



if __name__ == "__main__":
    main()