# Problem: Selection of Personnel - https://codeforces.com/problemset/problem/630/F

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
    n = read_int()
    res = math.comb(n, 5) + math.comb(n, 6) + math.comb(n, 7)
    print(res)
if __name__ == "__main__":
    #sys.setrecursionlimit(10**6)
    solve()
