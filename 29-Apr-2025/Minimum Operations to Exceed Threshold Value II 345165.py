# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        number_of_op = 0
        while len(nums) > 1 and  nums[0]<k:
            x,y = heappop(nums),heappop(nums)
            heappush(nums,2*x+y)
            number_of_op+=1
            
        return number_of_op