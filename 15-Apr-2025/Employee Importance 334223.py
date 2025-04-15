# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # first let me construct a graph for employee id
        graph = defaultdict(list)
        for emp in employees:
            graph[emp.id] = [emp.importance,emp.subordinates]

        importance = 0
        visitedId = set()
        def dfs(emp_id):
            nonlocal importance, visitedId
            importance+=graph[emp_id][0]

            visitedId.add(emp_id)
            for _id in graph[emp_id][1]:
                if _id not in visitedId:
                    dfs(_id)
        
        dfs(id)
        return importance