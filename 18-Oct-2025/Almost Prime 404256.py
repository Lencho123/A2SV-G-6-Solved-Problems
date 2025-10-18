# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

n = int(input())

def is_almost_prime(num):
    d = 2
    s = set()
    while num > 1:
        while num % d != 0:
            d+=1
        num/=d
        s.add(d)
    return len(s) == 2

res = 0
for i in range(1, n+1):
    res+=is_almost_prime(i)
print(res)
