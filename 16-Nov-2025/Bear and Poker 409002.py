# Problem: Bear and Poker - https://codeforces.com/problemset/problem/574/C

n = int(input())
a = [int(i) for i in input().split()]


def remove_32(num):
    n = num
    while n%2 == 0:
        n/=2
    while n%3 == 0:
        n/=3
    return n

pre = remove_32(a[0])
res = "Yes"
for i in range(1,len(a)):
    cur = remove_32(a[i])
    if pre != cur:
        res = "No"
        break
    pre = cur
    
print(res)