# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

t = int(input())
from collections import defaultdict

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    counts = defaultdict(int)

    def factorize(num):
        d = 2
        while num > 1:
            while num%d:
                d+=1
            num//=d
            counts[d]+=1
            
    for num in arr:
        factorize(num)
    
    res = "YES"
    for key in counts:
        if counts[key]%n:
            res = "NO"
            break
    print(res)
        