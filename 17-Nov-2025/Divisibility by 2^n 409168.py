# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D

from collections import defaultdict

t = int(input())
def count_two(num):
    count = 0
    while num > num%2 == 0:
        count+=1
        num/=2
    return count

for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]

    two_count = 0
    for num in a:
        two_count+=count_two(num)
    
    index_two = defaultdict(int)
    for i in range(1,n+1):
        if i % 2:
            continue
        index_two[i] = count_two(i)

    values = list(index_two.values())
    values.sort(reverse=True)

    res = 0
    for v in values:
        if two_count >= n:
            break
        two_count+=v
        res+=1

    
    if two_count >= n:
        print(res)
    else:
        print(-1)