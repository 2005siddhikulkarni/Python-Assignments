import threading

def Even():
    print("Even numbers are: ")
    for i in range(2,21,2):
        print(i)

def Odd():
    print("Odd numbers are: ")
    for i in range(1,20,2):
        print(i)

def main():
    t1 = threading.Thread(target = Even)
    t1.start()
    t1.join()

    t2 = threading.Thread(target = Odd)
    t2.start()
    t2.join()

    

if __name__ == "__main__":
    main()