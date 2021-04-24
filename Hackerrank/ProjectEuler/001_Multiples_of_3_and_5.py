#!/bin/python3

import sys


def sum_of_multiples(N):
    multiples_of_3 = (N - 1) // 3
    multiples_of_5 = (N - 1) // 5
    multiples_of_15 = (N - 1) // 15
    sum = (3 * multiples_of_3 * (multiples_of_3 + 1) // 2
           + 5 * multiples_of_5 * (multiples_of_5 + 1) // 2
           - 15 * multiples_of_15 * (multiples_of_15 + 1) // 2)
    return sum

if __name__ == '__main__':
    t = int(input("Test Cases : ").strip())
    for a0 in range(t):
        n = int(input("Sum of 3,5 below : ").strip())
        print("Result : ",sum_of_multiples(n))
    


#**********Output**********
# Test Cases : 2
# Sum of 3,5 below : 10
# Result :  23
# Sum of 3,5 below : 100
# Result :  2318