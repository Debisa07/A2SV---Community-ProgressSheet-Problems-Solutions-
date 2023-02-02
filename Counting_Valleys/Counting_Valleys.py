#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(n, s):
    level = 0
    num_valley = 0

    for i in s:
        if i == "U":
            level = level+1
        if i == "D":
            level = level -1
        if(level == 0 and i == "U"):
            num_valley += 1
    return num_valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()

    result = countingValleys(n, s)
    fptr.write(str(result) + '\n')
    fptr.close()