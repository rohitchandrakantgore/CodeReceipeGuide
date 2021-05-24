from functools import reduce

def filter_no(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            return num

def increaseBy(num):
    return num**2

def reduced(num1,num2):
    return num1 + num2


if __name__ == "__main__":
    numbers_array = [ int(x) for x in input("Enter List Elementd: ").split()]
    filered_list = list(filter(filter_no, numbers_array))
    print("Filtered List: ",filered_list)
    mapped_list = list(map(increaseBy,filered_list))
    print("Mapped List: ",mapped_list)
    reduced_result= reduce(reduced,mapped_list)
    print("Final Result: ",reduced_result)


# >python MarvellousAssignments/Assignment_4/Problem_5.py
# Enter List Elementd: 2 4 6 8 3 5 11
# Filtered List:  [2, 3, 5, 11]
# Mapped List:  [4, 9, 25, 121]
# Final Result:  159