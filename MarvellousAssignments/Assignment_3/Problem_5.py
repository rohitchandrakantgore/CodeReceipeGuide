from MarvellousNum import chkPrime

def add(numbers):
    addition = 0
    for i in range(len(numbers)):
        if chkPrime(numbers[i]):
            addition += numbers[i]

    return addition

if __name__=="__main__":
    numbersOfElements = int(input("numbersOfElements: "))
    numbers = []
    for i in range(numbersOfElements):
        numbers.append(int(input("Element {} : ".format(i))))

    print("Addition of all prime numbers in list: ", add(numbers))

# >python MarvellousAssignments/Assignment_3/Problem_5.py
# numbersOfElements: 6
# Element 0 : 2
# Element 1 : 4
# Element 2 : 6
# Element 3 : 7
# Element 4 : 11
# Element 5 : 13
# Addition of all prime numbers in list:  33