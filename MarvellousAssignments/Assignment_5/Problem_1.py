

def printn(num):
    while num>0:
        print('*', end=' ')
        return printn(num-1)

if __name__ =="__main__":
    num = int(input())
    printn(num)