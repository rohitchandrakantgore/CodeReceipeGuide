

class Circle:
    pi = 3.14
    def __init__(self, radius = 0, area=0, circumference=0):
        self.radius =radius
        self.area = area
        self.circumference = circumference
        # print(self.radius, self.circumference, self.area)

    def accept(self,radius):
        self.radius = radius 


    def calculateArea(self):
        self.area = self.pi * (self.radius**2)

    def calculateCircumference(self):
        self.circumference = 2* self.pi * self.radius

    def display(self):
        print("Radius : ",self.radius)
        print("Area : ",self.area)
        print("Circumference : ",self.circumference)

obj1 = Circle()
obj1.accept(3)
obj1.calculateArea()
obj1.calculateCircumference()
obj1.display()
print(" ")
obj2 = Circle()
obj2.accept(5)
obj2.calculateArea()
obj2.calculateCircumference()
obj2.display()


# >python MarvellousAssignments/Assignment_6/Problem_2.py
# Radius :  3
# Area :  28.26
# Circumference :  18.84

# Radius :  5
# Area :  78.5
# Circumference :  31.400000000000002