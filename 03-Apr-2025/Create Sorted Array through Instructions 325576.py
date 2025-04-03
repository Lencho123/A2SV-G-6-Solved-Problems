# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        
        for i,n in enumerate(instructions):
            instructions[i] = (n,i)
        # print(instructions)
        
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
                
            m=len(arr)//2
            left = mergeSort(arr[:m])
            right = mergeSort(arr[m:])

            return merge(left,right)
        
        def merge(left,right):
            numberOfSmall(left,right)

            l,r=0,0
            merged=[]
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

        def numberOfSmall(left,right):
            nonlocal small, large
            smallCount = 0
            l = 0
            for r in range(len(right)):
                while l < len(left) and right[r][0] > left[l][0]:
                    smallCount+=1
                    l+=1
                small[right[r][1]]+=smallCount

            largeCount = 0
            l = 0
            for r in range(len(right)):
                while l < len(left) and left[l][0]<=right[r][0]:
                    l+=1
                large[right[r][1]]+=len(left)-l

            
        small = [0 for i in range(len(instructions))]
        large = [0 for i in range(len(instructions))]

        mergeSort(instructions)
        totalCost = 0
        for i in range(len(instructions)):
            totalCost+=min(small[i], large[i])
        return (totalCost)%(10**9 + 7)
            