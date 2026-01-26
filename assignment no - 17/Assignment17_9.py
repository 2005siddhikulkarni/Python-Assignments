def CntNo(No):
    Cnt = 0
    for i in str(No):
        Cnt += 1

    return Cnt
        
def main():
    print("Enter the number: ")
    Value1 = int(input())
 
    Result = CntNo(Value1) 
    print(Result)
    

if __name__ == "__main__":
    main()