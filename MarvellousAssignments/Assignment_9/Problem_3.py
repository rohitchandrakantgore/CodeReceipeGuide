
filename = input('New file Name: ')


oldfile = open('demo.txt')
oldfileData = oldfile.readlines()[0]
oldfile.close()

newfiledata = open(filename, 'w+')
newfiledata.write(oldfileData)
newfiledata.seek(0)
print("Data Copied From OldFile: ",newfiledata.readlines()[0])
newfiledata.close()

# >python MarvellousAssignments/Assignment_9/Problem_3.py
# New file Name: demo2.txt
# Data Copied From OldFile:  Hello