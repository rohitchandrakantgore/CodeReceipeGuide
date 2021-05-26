
class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def deposite(self, amount):
        self.Amount+= amount
        print("Deposited: ", amount)

    def withdraw(self, amount):
        self.Amount -= amount
        print("Withdrawn: ", amount)

    def calculateIntrest(self):
        print("Rate Of Intreste: ",BankAccount.ROI * self.Amount)

    def display(self):
        print("Name: ", self.Name)
        print("Amount: ", self.Amount)
        print()


obj = BankAccount("ROhit", 1000)
obj.deposite(1000)
obj.calculateIntrest()
obj.display()
obj.withdraw(500)
obj.calculateIntrest()
obj.display()


# >Python MarvellousAssignments/Assignment_7/Problem_2.py
# Deposited:  1000
# Rate Of Intreste:  21000.0
# Name:  ROhit
# Amount:  2000

# Withdrawn:  500
# Rate Of Intreste:  15750.0
# Name:  ROhit
# Amount:  1500