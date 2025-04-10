# Problem: C - Ras Alula and The Decrypted Messages - https://codeforces.com/gym/601269/problem/C

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations
import sys
input = sys.stdin.readline
from math import ceil, floor, gcd, log2

def iinp(): return (int(input()))
def linp(): return (list(map(int, input().split())))
def sinp(): return (input().strip())
def minp(): return (map(int, input().split()))

t = iinp()  

for _ in range(t):
    n,m = linp()    
    s = sinp()
    w = sinp()
    
    spre = [0]
    for char in s:
        spre.append(spre[-1] + ord(char))
        
    window = 0
    flag = True
    for char in w:
        window += ord(char)
        l=0
        start = len(w)
        
    for r in range(start, n+1):
        if abs((spre[r] - spre[l]) - window) ==0:
            print("YES")
            flag = False
            break
            
        l+=1
    if flag:
        print("NO")
    