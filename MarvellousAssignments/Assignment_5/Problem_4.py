def sumofn(num):
    if num==0:
        return 0
    return (num%10) + (sumofn(num//10))

if __name__ =="__main__":
    num = int(input("Enter Number: "))    
    print("Sum of Digits: ",sumofn(num))

# >python MarvellousAssignments/Assignment_5/Problem_4.py
# Enter Number: 23124
# Sum of Digits:  12