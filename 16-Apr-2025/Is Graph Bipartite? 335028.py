# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        n = len(graph)
        
        color = [-1 for i in range(n)]

        def bfs(node):
            queue = deque([node])

            while queue:
                l=len(queue)
                for i in range(l):
                    p = queue.popleft()
                    for nei in graph[p]:
                        if color[p] == color[nei]:
                            return False
                        
                        if color[nei] == -1:
                            if color[p] == 0:
                                color[nei] = 1
                            else:
                                color[nei] = 0

                            queue.append(nei)

        for i in range(n):
            if color[i] == -1:
                color[i] = 0
                return_val = bfs(i)
                
                if return_val == False:
                    return False
        
        return True