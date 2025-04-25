# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        ingo = defaultdict(list)
        outgo = defaultdict(int)
        d = defaultdict(set)
        
        for u,v in prerequisites:
            graph[v].append(u)
            outgo[v]+=1
            ingo[u].append(v)
        
        que = deque([])
        
        for course in range(numCourses):
            if outgo[course] == 0:
                que.append(course)
                d[course] = set([])
        
        while que:
            p = que.popleft()
            for nd in ingo[p]:
                outgo[nd]-=1
                d[nd].add(p)
                d[nd].update(d[p])
                if outgo[nd] == 0:
                    que.append(nd)
        

        ans = []
        for q in queries:
            if q[0] in d[q[1]]:
                ans.append(True)
            else:
                ans.append(False)
        return ans