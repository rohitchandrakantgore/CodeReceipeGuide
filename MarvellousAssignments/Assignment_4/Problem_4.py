from functools import reduce

def filter_no(num):
    if num%2==0:
        return num 

def increaseBy(num):
    return num**2

def reduced(num1,num2):
    return num1 + num2

# reduce * all

if __name__ == "__main__":
    numbers_array = [ int(x) for x in input().split()]
    filered_list = list(filter(filter_no, numbers_array))
    print(filered_list)
    mapped_list = list(map(increaseBy,filered_list))
    print(mapped_list)
    reduced_result= reduce(reduced,mapped_list)
    print(reduced_result)



# (codenv) C:\Work\CodeRecipeGuide>python MarvellousAssignments/Assignment_4/Problem_4.py 
# 5 6 7 8 10 3 9 12
# [6, 8, 10, 12]
# [36, 64, 100, 144]
# 344
