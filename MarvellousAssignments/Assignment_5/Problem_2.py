
i=1
def printn(num):
    global i
    while num>0:
        print(i, end=' ')
        i+=1
        return printn(num-1)

if __name__ =="__main__":
    num = int(input())
    printn(num)

# >python MarvellousAssignments/Assignment_5/Problem_2.py                                        
# 5
# 1 2 3 4 5 