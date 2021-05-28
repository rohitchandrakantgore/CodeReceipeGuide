file1 = input('file1 name: ')
file2 = input('file2 name: ')

file1open = open(file1, 'r')
file2open = open(file2, 'r')

if file1open.readlines()== file2open.readlines():
    print("Same Data")
else:
    print("Not the Same")