import sys

def factn(num):
    if num ==0:
        return 1
    return num * factn(num-1)

num = int(input("Enter Number : "))
res =factn(num)
print("Factorial is: ",res)

# >python MarvellousAssignments/Assignment_5/Problem_5.py
# Enter Number : 6
# Factorial is:  720