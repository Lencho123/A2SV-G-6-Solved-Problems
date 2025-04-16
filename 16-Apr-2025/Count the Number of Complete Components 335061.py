# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # constuct graph
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(unvisited,node_count):
            nonlocal flag
            visited.add(unvisited)
            if node_count-1 != len(graph[unvisited]):
                flag = False

            for nei in graph[unvisited]:
                if nei not in visited:
                    dfs(nei,node_count)
        

        counted = set()
        count = 0
        flag = True

        def edgeCount(node):
            nonlocal count
            count+= 1
            counted.add(node)
            for nei in graph[node]:
                if nei not in counted:
                    edgeCount(nei)
            
        
        visited = set()
        res = 0
        for i in range(n):
            if i not in visited:
                count = 0
                edgeCount(i)
                flag = True
                dfs(i,count)
                res+=flag
        
        return res