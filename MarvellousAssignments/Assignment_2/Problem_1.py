from ArithmeticModule import Add, Sub, Mult,Div

num1, num2 = input("Enter Numbers : ").split(' ')

num1 = int(num1)
num2 = int(num2)
print("Add: ",Add(num1,num2))
print("Sub: ",Sub(num1,num2))
print("Mul: ",Mult(num1, num2))
print("Div: ",Div(num1, num2))

# >python MarvellousAssignments/Assignment_2/Problem_1.py
# Enter Numbers : 8 12
# Add:  20
# Sub:  -4
# Mul:  96
# Div:  0.6666666666666666