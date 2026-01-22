def PrimeorNot(Value1):
    Cnt = 0
    for i in range(1,Value1+1):
        if Value1 % i == 0 :
            Cnt += 1
        
    if Cnt == 2 :
        print(Value1,"is prime number") 

    else:
        print(Value1,"is not prime number")

def main():
    No1 = print("Enter the number: ")
    No1 = int(input())

    Result = PrimeorNot(No1)

if __name__ == "__main__":
    main()