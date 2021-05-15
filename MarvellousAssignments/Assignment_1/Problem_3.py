def Add(num1, num2):
    return int(num1)+ int(num2)

if __name__ == "__main__":
    num1, num2 = input("Enter Numbers : ").split(' ')
    res = Add(num1, num2)
    print(res)


### output ###
# >python MarvellousInfoSystems/Assignment_1/Problem_3.py
# Enter Numbers : 4 5
# 9