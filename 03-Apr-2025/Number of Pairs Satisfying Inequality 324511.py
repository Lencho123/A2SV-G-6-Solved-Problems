# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        diff_arr = []
        for n1,n2 in zip(nums1,nums2):
            diff_arr.append(n1-n2)
        
        def mergeSort(diff_arr):
            if len(diff_arr) <= 1:
                return diff_arr
            
            m = len(diff_arr)//2
        
            left = mergeSort(diff_arr[:m])
            right = mergeSort(diff_arr[m:])

            return merge(left,right)
        
        def merge(left,right):
            nonlocal res
            res+=countAns(left,right)
            merged = []

            l,r = 0,0
            while l < len(left) or r < len(right):
                if l == len(left):
                    merged.extend(right[r:])
                    break
                if r == len(right):
                    merged.extend(left[l:])
                    break
        
                if left[l] < right[r]:
                    merged.append(left[l])
                    l+=1
                else:
                    merged.append(right[r])
                    r+=1
            return merged
        
        def countAns(left,right):
            r = 0
            count = 0
            for l in range(len(left)):
                while r<len(right) and left[l] - right[r] > diff:
                    r+=1
                count+=len(right)-r
            return count
        
        res = 0
        mergeSort(diff_arr)
        return res