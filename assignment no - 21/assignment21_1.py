import threading

def ChkPrime(No):
    Cnt = 0
    if No <= 1:
        return False
    
    for i in range(1,No+1):
        if No % i == 0:
            Cnt += 1

    if Cnt == 2:
        return True
    
    else:
        return False
    
def Prime(lst):
    print("Prime numbers are: ")
    for i in range(len(lst)+1):
        if ChkPrime(i) == True:
            print(i)

def NonPrime(lst):
    print("Non prime numbers: ")
    for i in range(len(lst)+1):
        if ChkPrime(i) == False:
            print(i)

def main():
    lst = []

    print("Enter the no: ")
    No = int(input())

    print("enter the Values: ")
    for i in range(1,No+1):
        Values = int(input())
        lst.append(Values)

    t1 = threading.Thread(target = Prime , args = (lst,))
    t1.start()
    t1.join()

    t2 = threading.Thread(target = NonPrime , args = (lst,))
    t2.start()
    t2.join()

if __name__ == "__main__":
    main()