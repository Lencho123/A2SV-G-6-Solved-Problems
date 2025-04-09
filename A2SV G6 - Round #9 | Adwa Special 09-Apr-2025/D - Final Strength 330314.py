# Problem: D - Final Strength - https://codeforces.com/gym/601269/problem/D

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations
import sys
input = sys.stdin.readline

def iinp(): return (int(input()))
def linp(): return (list(map(int, input().split())))
def sinp(): return (input().strip())
def minp(): return (map(int, input().split()))

t = iinp()
for _ in range(t):
    n = iinp()
    a = linp()
    n = 2**n
    
    profit = [0 for i in range(n)]
    
    for i, n in enumerate(a):
        a[i] = (n, i)
    

    def mergeSort(arr):
        if len(arr) <= 1:
            return arr

        m = len(arr) // 2
        left = mergeSort(arr[:m])
        right = mergeSort(arr[m:])
        return merge(left, right)
    
    def merge(left, right):
        left, right = calculateProfit(left,right)
        l,r = 0,0
        merged = []
        while l < len(left) or r < len(right):
            if l == len(left):
                merged+= right[r:]
                break
            if r == len(right):
                merged+= left[l:]
                break
            if left[l][0] < right[r][0]:
                merged.append(left[l])
                l+=1
            else:
                merged.append(right[r])
                r+=1
        return merged
    
    def calculateProfit(left, right):
        runsum = 0
        r = 0
        strong_left = []
        strong_right = []
        for l in range(len(left)):
            while r < len(right) and right[r][0] < left[l][0]:
                runsum += 1
                r+=1
            strong_left.append((left[l][0]+runsum, left[l][1]))
        
        runsum = 0
        l = 0
        for r in range(len(right)):
            while l < len(left) and left[l][0] < right[r][0]:
                runsum += 1
                l+=1
            strong_right.append((right[r][0]+runsum, right[r][1]))
        
        return strong_left, strong_right
            
            
    final = mergeSort(a)
    res = [0 for i in range(len(final))]
    for i in range(len(final)):
        res[final[i][1]] = final[i][0]
        
    print(*res)
    