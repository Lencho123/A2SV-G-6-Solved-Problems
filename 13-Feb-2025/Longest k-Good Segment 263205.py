# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict

n,k =[int(i) for i in input().split()]
a=[int(i) for i in input().split()]

mx=1
dct=defaultdict(int)
count=0
l=0
mx_dist=1
res=[1,1]

for r in range(n):
    if dct[a[r]]==0:
        count+=1
    dct[a[r]]+=1
    
    while count > k:
        dct[a[l]]-=1
        if dct[a[l]]==0:
            count-=1
        l+=1
    
    if mx_dist < r-l+1:
        res=[l+1,r+1]
        mx_dist=r-l+1
print(*res)