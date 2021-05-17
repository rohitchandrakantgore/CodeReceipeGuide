
def add(numbers):
    res = 0
    for i in range(len(numbers)):
        res+=numbers[i]
    return res


if __name__=="__main__":
    numbersOfElements = int(input("numbersOfElements: "))
    numbers = []
    for i in range(numbersOfElements):
        numbers.append(int(input()))
    print("Sum is : ", add(numbers))
    

# >python MarvellousAssignments/Assignment_3/Problem_1.py 
# numbersOfElements: 4
# 5
# 67
# 34
# 0
# Sum is :  106