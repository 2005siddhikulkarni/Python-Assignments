
ongString = lambda S : len(S) > 5

def main():
    lst =  input("Enter Strings : ")

    Result = list(filter(LongString, lst))
    print("Long String is: ",Result)


if __name__ == "__main__":
    main()
