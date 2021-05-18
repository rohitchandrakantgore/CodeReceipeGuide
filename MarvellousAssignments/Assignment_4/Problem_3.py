from functools import reduce

def filter_no(num):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            return num

def increaseBy(num):
    return num*2

def reduced(num1,num2):
    if num1>num2:
        return num1
    else: 
        return num2

# reduce * all

if __name__ == "__main__":
    numbers_array = [ int(x) for x in input().split()]
    filered_list = list(filter(lambda x: x == i or x % i, numbers_array))
    print(filered_list)
    mapped_list = list(map(increaseBy,filered_list))
    print(mapped_list)
    reduced_result= reduce(reduced,mapped_list)
    print(reduced_result)


# >python MarvellousAssignments/Assignment_4/Problem_3.py                                        
# 80 90 88 78 89
# [80, 90, 88, 78, 89]
# [90, 100, 98, 88, 99]
# 7683984000