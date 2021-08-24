

def computeDifference(self):
    sortedlist = sorted(self.__elements)
    self.maximumDifference = abs(sortedlist[-1]-sortedlist[0])

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
