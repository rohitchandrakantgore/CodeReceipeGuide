
def chkPrime(num):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                return "Not Prime Number"
                break
        else:
            return "It is Prime Number"
    else:
        return "Not Prime Number"
if __name__=="__main__":
    num= int(input("Enter Number: "))
    print(chkPrime(num))

# >python MarvellousAssignments/Assignment_2/Problem_4.py
# Enter Number: 5
# It is Prime Number

# >python MarvellousAssignments/Assignment_2/Problem_4.py
# Enter Number: 6
# Not Prime Number