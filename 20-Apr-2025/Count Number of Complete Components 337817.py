# Problem: Count Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(n):
            graph[i] = []

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def bfs(node):
            nonlocal nodeCount, bl
            que = deque([node])

            while que:
                l = len(que)
                for i in range(l):
                    p = que.popleft()
                    if len(graph[p]) != len(graph[node]):
                        bl = False

                    for nei in graph[p]:
                        if nei not in visited:
                            que.append(nei)
                            nodeCount+=1
                            visited.add(nei)


        visited = set()
        count = 0

        for i in range(n):
            if i not in visited:
                visited.add(i)
                nodeCount = 1
                bl = True
                bfs(i)
                if bl and nodeCount-1 == len(graph[i]):
                    count+=1
        
        return count