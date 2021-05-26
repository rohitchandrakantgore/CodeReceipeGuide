class Numbers:

    def __init__(self,value):
        self.value = value
        print("Number: ", value)

    def checkPrime(self):
        if self.value>1:
            for i in range(2,self.value):
                if self.value % i ==0:
                    print("Not Prime")
                    break
            else:
                print("Prime")
        else:
            print("not Prime")

    def checkPerfect(self):
        sum = 0
        for i in range(1,self.value):
            if self.value%i==0:
                sum+= i
        if sum== self.value:
            print("Perfect Num")
        else:
            print("Not Perfect Num")

    def sumFactors(self):
        sum = 0
        for i in range(1,self.value):
            if self.value%i==0:
                sum+= i
        print("Sum Of Factors: ", sum)
        return sum

    def factors(self):
        factors_list=[]
        print("Factors are : ", end=' ')
        for i in range(1,self.value):
            if self.value%i==0:
                print(i, end=' ')
                factors_list.append(i)
        print()
        return factors_list

    def checkPerfect2(self):
        facs = self.factors()
        res=0
        for num in facs:
            res+= num
        if res == self.value:
            print("Prefect Num ")
        else:
            print("Not Prefect")

obj = Numbers(4)
obj.checkPrime()
obj.checkPerfect()
obj.factors()
obj.sumFactors()

obj.checkPerfect2()

print()
obj = Numbers(5)
obj.checkPrime()
obj.checkPerfect()
obj.factors()
obj.sumFactors()


# >Python MarvellousAssignments/Assignment_7/Problem_3.py
# Number:  4
# Not Prime
# Not Perfect Num
# Factors are :  1 2
# Sum Of Factors:  3
# Factors are :  1 2
# Not Prefect

# Number:  5
# Prime
# Not Perfect Num
# Factors are :  1
# Sum Of Factors:  1