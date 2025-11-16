# Problem: Row GCD - https://codeforces.com/problemset/problem/1458/a

import math
n,m = [int(i) for i in input().split()]

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

# use property of gcd(x,y,...,z) = gcd(x,y-x,...,z-x)
# gcd(bj+a1, bj+a2, bj+a3, ..., bj+an) #take x = bj+a1 and apply the property do for others too
# gcd(bj+a1, a2-a1, a3-a1,---, an-a1)

# let g = gcd(a2-a1, a3-a1, ..., an-a1)
# => gcd(bj + a1, g)
# IT IS THAT SIMPLE

g = 0
for i in range(1,n):
    g = math.gcd(g, abs(a[i]-a[0]))

ans = []
for num in b:
    ans.append(math.gcd(num + a[0], g))
print(*ans)
