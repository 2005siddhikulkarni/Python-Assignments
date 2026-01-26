import threading


    
def Max(lst):
    Max_Value = lst[0]
    for i in range(1,len(lst)+1):
        if i >= Max_Value:
            Max_Value = i
        
    print("Maximum value is: ",Max_Value)

def Min(lst):
    Min_Value = lst[0]
    for i in range(1,len(lst)+1):
       if i <= Min_Value:
            Min_Value = i
        
    print("Minimum value is: ",Min_Value)

def main():
    lst = []

    print("Enter the no: ")
    No = int(input())

    print("enter the Values: ")
    for i in range(1,No+1):
        Values = int(input())
        lst.append(Values)

    Thread1 = threading.Thread(target = Max , args = (lst,))
    Thread1.start()
    Thread1.join()

    Thread2 = threading.Thread(target = Min , args = (lst,))
    Thread2.start()
    Thread2.join()

if __name__ == "__main__":
    main()