
def SumEven(Value1):
    i = 0
    for i in range(2,Value1+1,2):
        print(i)

def main():
    No1 = print("Enter the number: ")
    No1 = int(input())

    SumEven(No1)
    

if __name__ == "__main__":
    main()