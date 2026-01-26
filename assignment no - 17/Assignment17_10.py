def SumOfNo(No):
    Total = 0
    for i in str(No):
        Total += int(i)
    return Total
        
def main():
    print("Enter the number: ")
    Value1 = int(input())
 
    Result = SumOfNo(Value1) 
    print(Result)
    

if __name__ == "__main__":
    main()