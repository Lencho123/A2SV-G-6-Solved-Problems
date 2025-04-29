# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)[-k:]
        heapq.heapify(self.nums)
        print(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums)==self.k:
            p = max(heappop(self.nums),val)
            heappush(self.nums,p)
        else:
            heappush(self.nums,val)

        return self.nums[0]
        
