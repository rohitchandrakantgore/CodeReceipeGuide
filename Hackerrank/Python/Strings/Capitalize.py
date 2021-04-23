#!/bin/python3

import math
import os
import random
import re
import sys


def solve(s):
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s  

if __name__ == '__main__':
    s = input("Enter String : ")
    result = solve(s)
    print("Capitalize Result : ",result)

#**********Output**********
# Enter String : alison heck
# Capitalize Result :  Alison Heck