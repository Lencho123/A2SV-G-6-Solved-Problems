# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

from collections import defaultdict

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n,m = [int(i) for i in input().split()]
    graph =  defaultdict(list)
    nodes = []
    for i in range(m):
        u, v = [int(i) for i in input().split()]
        graph[u].append(v)
        graph[v].append(u)
        nodes.append(u)
        nodes.append(v)

    def dfs(node):
        nonlocal cycle, extraNode
        visited.add(node)
        if len(graph[node]) != 2:
            extraNode = True
        for nei in graph[node]:
            if nei in visited:
                cycle = True
                continue
            dfs(nei)

    visited = set()
    count = 0
    for n in nodes:
        if n not in visited:
            cycle = False
            extraNode = False
            dfs(n)
            if cycle and not extraNode:
                count+=1

    print(count)
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
