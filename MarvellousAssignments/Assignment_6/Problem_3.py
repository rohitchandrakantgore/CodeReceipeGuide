
class Arithmetic:

    def __init__(self, value1 = 0,value2 =0):
        self.value1 = value1
        self.value2 = value2

    def accept(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
        return self.value1, self.value2

    def addition(self):
        return self.value2+ self.value1

    def subtraction(self):
        return self.value1 - self.value2

    def division(self):
        return self.value1 / self.value2

    def multiplication(self):
        return self.value1 * self.value2


obj = Arithmetic()
print("numbers enterd: ",obj.accept(10,20))
print("Addtion: ", obj.addition())
print("Subtraction: ", obj.subtraction())
print("Multiplication: ", obj.multiplication())
print("Division: ", obj.division())

# >python MarvellousAssignments/Assignment_6/Problem_3.py
# numbers enterd:  (10, 20)
# Addtion:  30     
# Subtraction:  -10
# Multiplication:  200
# Division:  0.5