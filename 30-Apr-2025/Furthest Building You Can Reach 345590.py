# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        heapq.heapify(heap)
        res = 0

        for i in range(1,len(heights)):
            d = heights[i]-heights[i-1]
            if d <= 0:
                res = i
                continue
            
            if bricks >= d:
                bricks-= d
                heappush(heap,-d)
                res = i
            elif ladders>0:
                if heap and -heap[0] > d:
                    p=heappop(heap)

                    bricks+=-p-d
                    heappush(heap,-d)

                ladders-=1
                res = i
            elif bricks < d and ladders == 0:
                break

        return res