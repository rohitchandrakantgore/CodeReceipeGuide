
def getMin(numbers):
    min = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i]< min:
            min = numbers[i]
    return min

if __name__=="__main__":
    numbersOfElements = int(input("numbersOfElements: "))
    numbers = []
    for i in range(numbersOfElements):
        numbers.append(int(input()))
    print("min is : ", getMin(numbers))


# >python MarvellousAssignments/Assignment_3/Problem_3.py
# numbersOfElements: 5
# 45
# 67
# 55
# 1
# 0
# min is :  0