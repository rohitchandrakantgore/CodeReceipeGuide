def ChkNum(num):
    if num==0:
        return "Zero"
    elif num>0:
        return "Positive Number"
    else:
        return "Negative Number"

if __name__=="__main__":
    num = int(input("Enter Number : "))
    print(ChkNum(num))


# >python MarvellousInfoSystems/Assignment_1/Problem_6.py 
# Enter Number : 0
# Zero

# >python MarvellousInfoSystems/Assignment_1/Problem_6.py
# Enter Number : 8
# Positive Number

# >python MarvellousInfoSystems/Assignment_1/Problem_6.py
# Enter Number : -9
# Negative Number