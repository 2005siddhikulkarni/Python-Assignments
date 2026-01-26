import threading

def EvenFactor(No):
    Sum = 0
    for i in range(1,No):
        if No % i == 0 and i % 2 == 0:
            Sum += i
    print("Sum of Even factor is: ",Sum)
        

def OddFactor(No):
    Sum = 0
    for i in range(1,No):
        if No % i == 0 and i % 2 != 0:
            Sum += i
    print("Sum of Odd factor is: ",Sum)
        

def main():
    print("Enter the number: ")
    Value = int(input())

    t1 = threading.Thread(target = EvenFactor , args = (Value,) )
    t1.start()
    t1.join()

    t2 = threading.Thread(target = OddFactor , args = (Value,))
    t2.start()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()