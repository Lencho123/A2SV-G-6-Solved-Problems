# Problem: Minimum Integer - https://codeforces.com/problemset/problem/1101/A

t = int(input())
import math

for _ in range(t):
    l,r,d = [int(i) for i in input().split()]
    if l/d > 1:
        print(d)
    else:
        print((math.ceil((r+1)/d))*d)