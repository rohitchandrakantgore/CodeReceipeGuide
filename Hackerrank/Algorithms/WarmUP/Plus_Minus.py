#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    n = len(arr)
    negatives, zeros, positives = 0,0,0
    for i in range(len(arr)):
        if arr[i]<0:
            negatives+= 1
        elif arr[i]==0:
            zeros+= 1
        else:
            positives+=1
    print("%.6f" %(positives/n))
    print("%.6f" %(negatives/n))
    print("%.6f" %(zeros/n))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)


#---------------------#

# 6
# -4 3 -9 0 4 1
# 0.500000
# 0.333333
# 0.166667
