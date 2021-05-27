from threading import Thread
from typing import AsyncGenerator

def evenSum(evenlist):
    sum=0
    for num in evenlist:
        if num%2==0:
            sum+=num
    print("EvenSum: ",sum)
    return sum

def oddSum(oddlist):
    sum=0
    for num in oddlist:
        if num%2!=0:
            sum+=num
    print("OddSum: ",sum)
    return num

if __name__=="__main__":
    evenlist= [int(x) for x in input("EvenList: ").split()]
    oddlist= [int(x) for x in input("Odd List: ").split()]

    evenlistThread = Thread(target= evenSum, args=(evenlist,))
    oddlistThread = Thread(target=oddSum, args=(oddlist,))

    evenlistThread.start()
    oddlistThread.start()


# >python MarvellousAssignments/Assignment_8/Problem_3.py
# EvenList: 10 20 30 55 67
# Odd List: 20 30 33 55 44
# EvenSum:  60
# OddSum:  88