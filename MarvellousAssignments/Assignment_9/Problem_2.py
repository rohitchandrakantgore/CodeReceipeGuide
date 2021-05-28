filename = input("file name: ")

try:
    f1 = open(filename)
    print("file data: ",f1.readlines()[0])
except:
    print("{} file Not Found !".format(filename))


# >python MarvellousAssignments/Assignment_9/Problem_2.py
# file name: demo.txt
# file data:  Hello