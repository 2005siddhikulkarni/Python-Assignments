def PrintingPtn(No):
    for i in range(No):
        for j in range(No):
            print("*",end = " ")

        print()

def main():
    print("Enter the number: ")
    Value1 = int(input())
 
    PrintingPtn(Value1) 

if __name__ == "__main__":
    main()