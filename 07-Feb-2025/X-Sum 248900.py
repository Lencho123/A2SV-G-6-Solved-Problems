# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

from collections import defaultdict

t=int(input())
for test in range(t):
    n,m = [int(_) for _ in input().split()]

    arr=[]
    for i in range(n):
        row=list(map(int, input().split()))
        arr.append(row)
    r_diagonal=defaultdict(int)
    l_diagonal=defaultdict(int)
    
    for i in range(n):
        for j in range(m):
            r_key=i-j
            l_key=i+j #+ n+m #take offset by n+m to aboid key overlap
            r_diagonal[r_key]+=arr[i][j]
            l_diagonal[l_key]+=arr[i][j]
    mx=0
    for i in range(n):
        for j in range(m):
            profit=r_diagonal[i-j]+l_diagonal[i+j]-arr[i][j]
            mx=max(mx,profit)
    print(mx)
            
    