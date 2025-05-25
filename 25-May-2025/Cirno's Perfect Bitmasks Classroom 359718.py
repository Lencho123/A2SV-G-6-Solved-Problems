# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

t = int(input())

for _ in range(t):
    n = int(input())
    i = 0
    while n&i == 0 or n^i == 0:
        i+=1
    print(i)