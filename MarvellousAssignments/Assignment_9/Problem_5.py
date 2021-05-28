
filename = input("filename: ")
searchstring = input("search string: ")

fileopen = open(filename,'r')
data = fileopen.readlines()[0]

print("frequency: ",str(data.count(searchstring)))

# >python MarvellousAssignments/Assignment_9/Problem_5.py
# filename: demo.txt
# search string: Hello
# frequency:  1