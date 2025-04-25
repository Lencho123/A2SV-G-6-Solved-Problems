# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        in_going = defaultdict(list)
        out_edge_count = defaultdict(int)
        que = deque([])
        res = []

        for i, edges in enumerate(graph):
            for nod in edges:
                in_going[nod].append(i)
            out_edge_count[i] = len(edges)
            if len(edges) == 0:
                que.append(i)
                res.append(i)
        

        while que:
            p = que.popleft()
            for nod in in_going[p]:
                out_edge_count[nod]-=1
                if out_edge_count[nod] == 0:
                    que.append(nod)
                    res.append(nod)
                    
        return sorted(res)