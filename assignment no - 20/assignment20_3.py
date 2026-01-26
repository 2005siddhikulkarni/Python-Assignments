import threading

def EvenList(lst):
    Sum = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            Sum += i
    print("Sum of Even of elements is: ",Sum)
        

def OddList(lst):
    Sum = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            Sum += i
    print("Sum of Odd elements is: ",Sum)
        

def main():
    lst = []
    print("Enter the number: ")
    No = int(input())
    
    print("Enter the numbers: ")

    for i in range(1,No+1):
        Values = int(input())
        lst.append(Values)

    t1 = threading.Thread(target = EvenList , args = (lst,) )
    t2 = threading.Thread(target = OddList , args = (lst,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    

if __name__ == "__main__":
    main()