
def factadd(num):
    factor = [1]
    for i in range(2, num+1):
        if num%i==0:
            factor.append(i)
    return sum(factor)

num = int(input("enter no: "))
print("sum of factors is: ", factadd(num))

# >python MarvellousAssignments/Assignment_2/Problem_4.py
# enter no: 30
# sum of factors is:  72