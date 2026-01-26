import threading


    
def Sum(lst):
    Sum = 0
    for i in range(1,len(lst)+1):
        Sum += i
    print("Sum is: ",Sum)
    
def Product(lst):
    Multiplication = 1
    for i in range(1,len(lst)+1):
        Multiplication *= i
    print("Multiplication is: ",Multiplication)

def main():
    lst = []

    print("Enter the no: ")
    No = int(input())

    print("enter the Values: ")
    for i in range(1,No+1):
        Values = int(input())
        lst.append(Values)

    Thread1 = threading.Thread(target = Sum , args = (lst,))
    Thread1.start()
    Thread1.join()

    Thread2 = threading.Thread(target = Product , args = (lst,))
    Thread2.start()
    Thread2.join()

if __name__ == "__main__":
    main()