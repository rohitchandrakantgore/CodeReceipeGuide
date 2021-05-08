from collections import Counter
n = int(input("No Of Shoes : "))
s = Counter(map(int,input("Shoe Sizes : ").split()))
x = int(input("No Of Customers: "))
total = []
for i in range(x):
    a,b = map(int,input("shoe no. and amount paid : ").split())
    if s[a] > 0:
        total.append(b)
        s.subtract(Counter([a]))
    else:
        pass

print("Amount Earned : ",sum(total))


### Output ###
# No Of Shoes : 5
# Shoe Sizes : 4 6 8 9 5
# No Of Customers: 4 
# shoe no. and amount paid : 5 50
# shoe no. and amount paid : 6 70
# shoe no. and amount paid : 8 100
# shoe no. and amount paid : 4 80
# Amount Earned :  300