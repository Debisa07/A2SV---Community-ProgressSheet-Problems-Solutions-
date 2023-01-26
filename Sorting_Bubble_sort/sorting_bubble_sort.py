#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#
def countSwaps(a):
    count = 0

    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[j] < a[i]:
                a[i] = a[i]+a[j]
                a[j] = a[i]-a[j]
                a[i] = a[i] - a[j]
                count += 1

    print('Array is sorted in {} swaps.'.format(count))
    print('First Element:', a[0])
    print('Last Element:', a[-1])

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))
    countSwaps(a)