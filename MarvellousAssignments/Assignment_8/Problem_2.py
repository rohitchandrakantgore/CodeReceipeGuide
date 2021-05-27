import threading
from typing import AsyncGenerator

def oddFactor(num):
    sum =0
    oddFacts=[]
    for i in range(1,num):
        if num%i==0:
            if i%2!=0:
                sum+=i
                oddFacts.append(i)
    print("Odd Factors: {} and Sum: {}".format(oddFacts, sum))
    print("Exit From Main(odd) Thread")
    return sum

def evenFactor(num):
    sum =0
    evenFacts=[]
    for i in range(1,num):
        if num%i==0:
            if i%2==0:
                sum+=i
                evenFacts.append(i)
    print("Even Factors: {} and Sum: {}".format(evenFacts,sum))
    return sum


if __name__=="__main__":
    num = int(input("Enter Number: "))

    oddFactorThread = threading.Thread(target=oddFactor, args=(num,))
    evenFactorThread = threading.Thread(target=evenFactor, args=(num,))
    oddFactorThread.start()
    evenFactorThread.start()
    oddFactorThread.join()
    evenFactorThread.join()


# >python MarvellousAssignments/Assignment_8/Problem_2.py
# Enter Number: 1000
# Odd Factors: [1, 5, 25, 125] and Sum: 156
# Exit From Main(odd) Thread
# Even Factors: [2, 4, 8, 10, 20, 40, 50, 100, 200, 250, 500] and Sum: 1184
