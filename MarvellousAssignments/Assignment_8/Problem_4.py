
from threading import Thread
import threading

def smallLet(str):
    smallCase = []
    for ch in str:
        if ch.islower():
            smallCase.append(ch)
    print("LowerCase: ",smallCase)

def UpperLet(str):
    UpperCase = []
    for ch in str:
        if ch.isupper():
            UpperCase.append(ch)
    print("UpperCase: ",UpperCase)

def digitLet(str):
    digitCase = []
    for ch in str:
        if ch.isnumeric():
            digitCase.append(ch)
    print("NumericCase: ",digitCase)


if __name__=="__main__":
    name = input("Enter String: ")

    smallThread = Thread(target=smallLet, args=(name,))
    capitalThread = Thread(target=UpperLet, args=(name,))
    digitTherad = Thread(target=digitLet, args=(name,))
    smallThread.run()
    print("Current Thread: ",threading.current_thread().name)
    print("Thread Id: ",threading.get_ident())    
    capitalThread.start()
    digitTherad.start()


# >python MarvellousAssignments/Assignment_8/Problem_4.py
# Enter String: RohitGore22jan
# LowerCase:  ['o', 'h', 'i', 't', 'o', 'r', 'e', 'j', 'a', 'n']
# Current Thread:  MainThread
# Thread Id:  18980
# UpperCase:  ['R', 'G']
# NumericCase:  ['2', '2']