# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

from collections import defaultdict 

n,m = [int(i) for i in input().split()]

array = []
for i in range(m):
    u, v = [int(i) for i in input().split()]
    array.append((u,v))

graph = defaultdict(list)
for u, v in array:
    graph[u].append(v)
    graph[v].append(u)
    
def bus(graph):
    count1 = 0
    count2 = 0
    for i in graph:
        if len(graph[i]) == 1:
            count1 += 1
        elif len(graph[i]) == 2:
            count2 += 1
    return count1 == 2 and count2 == n-2

def ring(graph):
    count2 = 0
    for i in graph:
        if len(graph[i]) == 2:
            count2 += 1
    return count2 == n

def star(graph):
    count1 = 0
    countn1 = 0
    for i in graph:
        if len(graph[i]) == 1:
            count1 += 1
        elif len(graph[i]) == n-1:
            countn1 += 1
    return count1 == n-1 and countn1 == 1

if bus(graph):
    print("bus topology")
elif ring(graph):
    print("ring topology")
elif star(graph):
    print("star topology")
else:
    print("unknown topology")