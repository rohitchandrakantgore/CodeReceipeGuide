def reverseArray(a):
    res = []
    for i in range(len(a)-1,-1,-1):
        res.append(a[i])
    return res

array = [1,2,3,4]
print("Reversed Array: ",reverseArray(array))


# >Python Hackerrank/DataStructure/Arrays/RevereseArray.py
# Reversed Array:  [4, 3, 2, 1]
