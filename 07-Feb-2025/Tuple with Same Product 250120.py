# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count=defaultdict(int)
        nums.sort()
        num_of_tuple=0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product=nums[i]*nums[j]
                num_of_tuple+=count[product]
                count[product]+=1

        return 8*num_of_tuple

 