def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        sub = string[i:i+k]
        res=set()
        for i in sub:
            if i not in res:
                print(i,end='')
                res.add(i)
        print('')

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# >python Hackerrank/Python/Strings/merge_the_tools.py
# AAASSSDSAAASSSD
# 3
# A
# S
# DSA
# AS
# SD