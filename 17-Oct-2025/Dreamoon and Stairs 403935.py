# Problem: Dreamoon and Stairs - https://codeforces.com/problemset/problem/476/A

n,m = [int(i) for i in input().split()]

candidate = (n//2) + n%2
while candidate%m:
    candidate+=1

if m > n:
    candidate = -1
print(candidate)