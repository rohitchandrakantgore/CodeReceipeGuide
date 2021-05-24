
class Demo:
    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2

    def fun(self):
        return self.no1, self.no2

    def gun(self):
        return self.no1, self.no2

obj1 = Demo(11,21)
obj2 = Demo(51,101)
print(obj1.fun())
print(obj2.fun())

print(obj1.gun())
print(obj2.gun())