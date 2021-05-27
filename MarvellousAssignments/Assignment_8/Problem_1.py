import threading

def even(limit):
    print("Even Numbers: ")
    for i in range(2,limit*2+1,2):
        print(i)

def odd(limit):

    print("Odd Numbers: ")
    for i in range(1,limit*2+1,2):
        print(i)

if __name__ =="__main__":
    limit = int(input("target: "))
    t1 =threading.Thread(target=even, args=(limit,))
    t2= threading.Thread(target=odd, args=(limit,))
    t1.run()
    t2.run()

# >python MarvellousAssignments/Assignment_8/Problem_1.py
# target: 10
# Even Numbers:
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20
# Odd Numbers:
# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 17
# 19
