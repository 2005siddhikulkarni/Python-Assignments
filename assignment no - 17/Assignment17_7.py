def PrintingNo(No):
    for i in range(No):
        for j in range(1,No+1):
            print(j,end = " ")

        print()

def main():
    print("Enter the number: ")
    Value1 = int(input())
 
    PrintingNo(Value1) 

if __name__ == "__main__":
    main()