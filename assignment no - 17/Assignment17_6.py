def PrintingPtn(No):
    for i in range(1,No+1):
        for j in range(i,0,-1):
            print("*",end = " ")

        print()

def main():
    print("Enter the number: ")
    Value1 = int(input())
 
    PrintingPtn(Value1) 

if __name__ == "__main__":
    main()