# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        nset=set(nums)
        unique=list(nset)

        def count(val):
            return counter[val]

        res=[]
        sorted_unique=sorted(unique, key=count, reverse=True)

        return sorted_unique[:k]