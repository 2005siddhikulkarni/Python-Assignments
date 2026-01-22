
def PrintFactors(Value1):
    for i in range(1,Value1+1):
        if Value1 % i == 0 :
            print(i)

def main():
    No1 = print("Enter the number: ")
    No1 = int(input())

    Result = PrintFactors(No1)

if __name__ == "__main__":
    main()