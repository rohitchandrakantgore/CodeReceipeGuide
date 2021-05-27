import threading

def ints():
    for i in range(1,51):
        print(i)

def revs():
    for i in range(50,0,-1):
        print(i)

if __name__=="__main__":
    thread1 = threading.Thread(target=ints)
    thread2 = threading.Thread(target=revs)
    thread1.start()
    thread1.join()
    thread2.start()
    thread2.join()