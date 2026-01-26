def PrimeNo(No):
    Cnt = 0
    for i in range(1,No+1):
        if No % i == 0:
            Cnt +=1
    
    if Cnt == 2:
        print("Prime number")

    else :
        print("Not a prime number")


def main():
    print("Enter the number: ")
    Value1 = int(input())
 
    PrimeNo(Value1)

if __name__ == "__main__":
    main()