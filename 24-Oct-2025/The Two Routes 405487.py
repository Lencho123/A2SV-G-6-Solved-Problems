# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A

import sys
import math
import bisect
import heapq
import random
from collections import defaultdict, deque, Counter
from itertools import combinations, permutations

# ---------- Constants ----------
MOD = 10**9 + 7
INF = float('inf')
RAND = random.randint(1, 2**31)

# ---------- Directions ----------
DIR4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
DIR8 = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]

def dir4(x, y): return [(x, y), (x, -y), (-x, y), (-x, -y)]
def dir8(x, y): return [(x, y), (x, -y), (-x, y), (-x, -y), (y, x), (y, -x), (-y, x), (-y, -x)]

# ---------- Fast Input ----------
def read_int(): return int(sys.stdin.readline())
def read_str(): return sys.stdin.readline().strip()
def read_ints(): return list(map(int, sys.stdin.readline().split()))
def read_list(): return sys.stdin.readline().split()  # for strings

# ---------- Math Helpers ----------
def lcm(a, b): return a * b // math.gcd(a, b)
def ceil_div(a, b): return (a + b - 1) // b
def mod_add(a, b): return (a + b) % MOD
def mod_mul(a, b): return (a * b) % MOD

# ---------- Binary Search ----------
def lower_bound(arr, x): return bisect.bisect_left(arr, x)
def upper_bound(arr, x): return bisect.bisect_right(arr, x)

# ---------- Heap Helpers ----------
def push(heap, item): heapq.heappush(heap, item)
def pop(heap): return heapq.heappop(heap)
def heapify_list(arr): heapq.heapify(arr)

# ---------- Utils ----------
def debug(*args): print("DEBUG:", *args, file=sys.stderr)
def inside(x, y, n, m): return 0 <= x < n and 0 <= y < m

# ---------- Example Main ----------
def solve():
    n,m = read_ints()
    realway_edges = set()
    for _ in range(m):
        u,v = read_ints()
        realway_edges.add((u,v))

    
    # construct graph for both realways and roads
    real_graph = defaultdict(list)
    road_graph = defaultdict(list)

    for u,v in realway_edges:
        real_graph[u].append(v)
        real_graph[v].append(u)

    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if (j,i) not in realway_edges and (i,j) not in realway_edges:
                road_graph[i].append(j)
                road_graph[j].append(i)


    real_time = {i:float("inf") for i in range(1,n+1)}
    road_time = {i:float("inf") for i in range(1,n+1)}

    # set time = 0 for original node(1)
    real_time[1] = 0
    road_time[1] = 0

    # calculate single point shorters time form origin(1) to other use(Diksjra sortestpath) for realway
    heap = []


    # t=0 to reach node 1
    push(heap,(0,1))
    visited = set()
    
    while heap:
        fro_time, fro = pop(heap)
        if fro in visited:
            continue
        visited.add(fro)

        for to in real_graph[fro]:
            real_time[to] = min(real_time[to], real_time[fro] + 1)

            push(heap, (real_time[to], to))


    # DO FOR ROAD ALSO BY CHECKING NOT ARRIEVE TO THE SAME TOWN AT SAME TIME EXCEPT END TWON
    # calculate single point shorters time form origin(1) to other use(Diksjra sortestpath) for road
    heap = []


    # t=0 to reach node 1
    push(heap,(0,1))
    visited = set()
    
    while heap:
        fro_time, fro = pop(heap)
        if fro in visited:
            continue
        visited.add(fro)

        for to in road_graph[fro]:
            road_time[to] = min(road_time[to], road_time[fro] + 1)
            if road_time[to] == real_time[to] and n != to:
                road_time[to] = float("inf")
            push(heap, (road_time[to], to))


    res = max(real_time[n],road_time[n])
    if res != float("inf"):
        print(res)
    else:
        print(-1)

if __name__ == "__main__":
    # sys.setrecursionlimit(10**3)
    solve()
