# Problem: Destroying Bridges - https://codeforces.com/problemset/problem/1944/A

t = int(input())

for _ in range(t):
    n,k = [int(i) for i in input().split()] 
    
    if k >= n-1:
        print(1)
    else:
        print(n)
        