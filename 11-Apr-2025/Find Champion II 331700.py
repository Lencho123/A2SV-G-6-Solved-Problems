# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if not edges and n == 1:
            return 0
        
        graph = defaultdict(set)
        
        for u,v in edges:
            graph[u].add(v)
        
        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    if nei in graph:
                        dfs(nei)
                    else:
                        visited.add(nei)
        
        for node in graph:
            visited = set()
            dfs(node)
            if len(visited) == n:
                return node
            visited = set()
        return -1     