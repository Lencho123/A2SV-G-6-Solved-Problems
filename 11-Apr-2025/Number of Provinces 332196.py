# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(set)
        row,col = len(isConnected), len(isConnected[0])

        for i in range(row):
            for j in range(col):
                if isConnected[i][j] == 1:
                    graph[i].add(j)
                    graph[j].add(i)

        
        def visit(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    visit(nei)
        
        count = 0
        visited = set()
        for node in graph:
            if node not in visited:
                count += 1
                visit(node)

        # print(graph)
        return count