# Problem: Reverse Pairs - https://leetcode.com/problems/reverse-pairs/description/

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            
            m = len(arr)//2
            left = mergeSort(arr[:m])
            right = mergeSort(arr[m:])
            
            return merge(left,right)
        
        def merge(left,right):
            countReverse(left,right)
            merged = []

            l,r = 0,0
            while l < len(left) or r < len(right):
                if l == len(left):
                    merged+=right[r:]
                    break
                if r == len(right):
                    merged+=left[l:]
                    break
                
                if left[l] < right[r]:
                    merged.append(left[l])
                    l+=1
                else:
                    merged.append(right[r])
                    r+=1
            return merged
        
        def countReverse(left,right):
            nonlocal res
            r = 0

            runsum = 0
            for l in range(len(left)):
                while r < len(right) and left[l] > right[r]*2:
                    runsum+=1
                    r+=1
                res+=runsum
        
        res = 0
        mergeSort(nums)
        return res
