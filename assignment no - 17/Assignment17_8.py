def PrintingNo1(No):
    for i in range(1,No+1):
        for j in range(1,i+1):
            print(j,end = " ")

        print()

def main():
    print("Enter the number: ")
    Value1 = int(input())
 
    PrintingNo1(Value1) 

if __name__ == "__main__":
    main()