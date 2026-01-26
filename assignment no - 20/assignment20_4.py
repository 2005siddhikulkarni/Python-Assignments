import threading

def Small(S):
    print(threading.current_thread().name)
    print(threading.get_ident())
    Cnt = 0
    for i in S:
        if i =="":
            Cnt += 1
    print("Count of small characters is: ",Cnt)

def Capital(S):
    print(threading.current_thread().name)
    print(threading.get_ident())
    Cnt = 0
    for i in S:
        if i >= "A" and i <= "Z":
            Cnt += 1
    print("Count of capital characters is: ",Cnt)  
        
def Digits(S): 
    print(threading.current_thread().name)
    print(threading.get_ident())
    Cnt = 0
    for i in S:
        if i >= "0" and i <= "9":
            Cnt += 1
    print("Count of digital numbers is: ",Cnt)

def main():
    print(threading.current_thread().name)
    print(threading.get_ident())
    
    print("Enter the string: ")
    S = input()
    
    t1 = threading.Thread(target = Small , args = (S,) )
    t1.start()
    t1.join()

    t2 = threading.Thread(target = Capital , args = (S,))
    print()
    t2.start()
    t2.join()

    t3 = threading.Thread(target = Digits , args = (S,))
    t3.start()
    t3.join()

    

if __name__ == "__main__":
    main()