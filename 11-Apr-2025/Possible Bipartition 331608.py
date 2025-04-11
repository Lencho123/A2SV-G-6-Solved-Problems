# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # construct graph

        graph = defaultdict(set)
        for u,v in dislikes:
            graph[v].add(u)
            graph[u].add(v)
        
        def dfs(node):
            for nei in graph[node]:
                
                if nei in visited:
                    if (nei in group1 and node in group1) or (nei in group2 and node in group2):
                        return False
                    continue
                
                if node in group1:
                    group2.add(nei)
                    visited.add(nei)
                    found = dfs(nei)
                    if found == False: 
                        return False
                else:
                    group1.add(nei)
                    visited.add(nei)
                    found = dfs(nei)
                    if found == False:
                        return False
            return True

        group1=set()
        group2 = set()
        visited = set()
        for node in graph:
            if node not in visited:
                group1.add(node)
                can_be_grouped = dfs(node)
                if not can_be_grouped:
                    return False
        return True
   