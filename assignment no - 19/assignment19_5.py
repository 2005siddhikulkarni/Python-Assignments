import functools 

def ChkPrime(A):
    Cnt = 0
    if A <= 1:
        return False
    
    for i in range(1,A+1):
        if A % i == 0:
            Cnt += 1

    if Cnt == 2:
        return True
    
    else :
        return False
        
MData = lambda A: A * 2
RData = lambda A,B: A if A > B else B


def main():
    lst = []

    print("Enter the number: ")
    No = int(input())

    print("Enter the elements: ")
    for i in range(No):
        Values = int(input())
        lst.append(Values)

    Result1 = list(filter(ChkPrime, lst))
    print("list after filter is: ",Result1)

    Result2 = list(map(MData, Result1))
    print("list after map is: ",Result2)

    Result3 = functools.reduce(RData, Result2)
    print("list after filter is: ",Result3)
   

if __name__ == "__main__":
    main()