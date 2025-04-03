# Problem: Count of Smaller Numbers After Self - https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0 for i in range(len(nums))]

        nums.reverse()
        for i,n in enumerate(nums):
            nums[i] = (n,i)
        
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            
            m = len(arr)//2
            left = mergeSort(arr[:m])
            right = mergeSort(arr[m:])

            return merge(left,right)
        
        def merge(left,right):
            calculateSmall(left,right)
            merged = []
            l,r = 0,0

            while l < len(left) or r < len(right):
                if l == len(left):
                    merged+=right[r:]
                    break

                if r == len(right):
                    merged+=left[l:]
                    break

                if left[l][0] < right[r][0]:
                    merged.append(left[l])
                    l+=1
                else:
                    merged.append(right[r])
                    r+=1
            return merged
    
        def calculateSmall(left,right):
            nonlocal res
            count = 0
            l = 0
            for r in range(len(right)):
                while l < (len(left)):
                    if left[l][0] < right[r][0]:
                        count+=1
                        l+=1
                    else:
                        break
                res[right[r][1]]+=count
        
        mergeSort(nums)
        res.reverse()
        return res