
def searchElement(numbers,elementTosearch):
    count = 0
    for i in range(len(numbers)):
        if numbers[i]==elementTosearch:
            count+=1
    return count

if __name__=="__main__":
    numbersOfElements = int(input("numbersOfElements: "))
    numbers = []
    for i in range(numbersOfElements):
        numbers.append(int(input("Element {} : ".format(i))))
    elementTosearch= int(input("Element To Search: "))
    print("{0} appered {1} times".format(elementTosearch,searchElement(numbers,elementTosearch)))


# >python MarvellousAssignments/Assignment_3/Problem_4.py
# numbersOfElements: 5 
# Element 0 : 4
# Element 1 : 5
# Element 2 : 6
# Element 3 : 4
# Element 4 : 5
# Element To Search: 4
# 4 appered 2 times
