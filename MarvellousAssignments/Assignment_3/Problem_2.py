
def getMax(numbers):
    max = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i]> max:
            max = numbers[i]
    return max

if __name__=="__main__":
    numbersOfElements = int(input("numbersOfElements: "))
    numbers = []
    for i in range(numbersOfElements):
        numbers.append(int(input()))
    print("max is : ", getMax(numbers))



# >python MarvellousAssignments/Assignment_3/Problem_2.py                                        
# numbersOfElements: 5
# 9   
# 77
# 779 
# 56
# 4
# max is :  779