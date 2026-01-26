import threading

Cnt = 0
lock_obj = threading.Lock()

def update():
    global Cnt

    for _ in range(1000):
        with lock_obj:
            Cnt = Cnt + 1




def main():
    global iCnt
    
    t1 = threading.Thread(target=update)
    t2 = threading.Thread(target=update)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Value of iCnt: ",Cnt)


if __name__ =="__main__":
    main()

