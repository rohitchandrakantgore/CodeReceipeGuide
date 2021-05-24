
def printn(num):
    while num>0:
        print(num, end=' ')
        return printn(num-1)

if __name__ =="__main__":
    num = int(input())
    printn(num)

# >python MarvellousAssignments/Assignment_5/Problem_3.py 
# 5
# 5 4 3 2 1 