# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        # construct graph
        graph = defaultdict(list)
        for i,id in enumerate(manager):
            graph[id].append(i)

        def dfs(index):
            # basecase
            visited.add(index)

            if not graph[index]:
                return informTime[index]
            
            mx_time = 0
            for sub in graph[index]:
                if sub not in visited:
                    mx_time = max(mx_time, dfs(sub))

            return informTime[index] + mx_time
        
        visited = set()
        return dfs(headID)         