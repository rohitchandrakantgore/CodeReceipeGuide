import math
import os
import random
import re
import sys
import collections



if __name__ == '__main__':
    s = input("Enter Company Name : ").strip()
    res_ =  collections.Counter(s).most_common()
    res_ = sorted(res_,key= lambda x: (x[1] *-1 , x[0]))
    for i in range(0,3):
        print(res_[i][0],res_[i][1] )


### output ###
# Enter Company Name : gadgetsandgeeks
# e 3
# g 3
# a 2