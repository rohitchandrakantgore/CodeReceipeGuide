def ChkNum(num):
    if num %2 ==0:
        return "Even Number"
    else:
        return "Odd Number"


if __name__ == "__main__":
    num = int(input('Enter A Number to Check is it Even Or Odd: '))
    res = ChkNum(num)
    print(res)


### output ###

# >python MarvellousInfoSystems/Assignment_1/Problem_2.py 
# Enter A Number to Check is it Even Or Odd: 8
# Even Number

# >python MarvellousInfoSystems/Assignment_1/Problem_2.py
# Enter A Number to Check is it Even Or Odd: 11
# Odd Number

