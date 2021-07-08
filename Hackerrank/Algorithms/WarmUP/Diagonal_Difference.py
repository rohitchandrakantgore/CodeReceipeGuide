#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    sum1,sum2 = 0,0
    for i in range(len(arr)):
        sum1+= arr[i][i]
    for i in range((len(arr))):
        sum2+= arr[i][len(arr)-1-i]
    return abs(sum1-sum2)
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)


#----------------------------#
# 3
# 11 2 4
# 4 5 6
# 10 8 -12
# 15