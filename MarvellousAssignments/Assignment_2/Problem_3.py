import math

def factmath(num):
    return math.factorial(num)

#iterative
def fact(num):
    if num==1 or num==0:
        return num
    else:
        return num* fact(num-1)

if __name__ == "__main__":
    num = int(input("Enter Num: "))
    print("iterative Factorial is: ",fact(num))
    print("math factorial is: ", factmath(num))


# >python MarvellousAssignments/Assignment_2/Problem_3.py
# Enter Num: 6
# iterative Factorial is:  720
# math factorial is:  720