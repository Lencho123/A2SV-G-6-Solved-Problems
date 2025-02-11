# Problem: Bubble Sort - https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

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
    # Write your code here
    swap=0
    for i in range(len(a)):
        for j in range(1,len(a)-i):
            if a[j]<a[j-1]:
                a[j],a[j-1]=a[j-1],a[j]
                swap+=1
    return swap

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
        
    print('Array is sorted in '+ str(countSwaps(a)) +' swaps.')
    print('First Element: '+ str(a[0]))
    print('Last Element: '+ str(a[-1]))
