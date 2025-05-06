# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i, ts in enumerate(tasks):
            start, pro_t = ts
            tasks[i] = (start, pro_t, i)
        
        tasks.sort()
        time = tasks[0][0]
        i = 0
        res = []
        heap = []

        while i < len(tasks):
            # collect available tsks
            while i < len(tasks) and time >= tasks[i][0]:
                heappush(heap,(tasks[i][1],tasks[i][2]))
                i+=1
            
            if not heap:
                heappush(heap,(tasks[i][1],tasks[i][2]))
                time = tasks[i][0]
                i+=1
            
            # process
            p = heappop(heap)
            res.append(p[1])
            time+=p[0]
            

        while heap:
            res.append(heappop(heap)[1])

        return res