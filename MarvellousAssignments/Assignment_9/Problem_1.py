filename = input("file name: ")

try:
    f1 = open(filename)
except:
    print("{} file Not Found !".format(filename))

# >python MarvellousAssignments/Assignment_9/Problem_1.py
# file name: demo.txt
# demo.txt file Not Found !