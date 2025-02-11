# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #   MERGE SORT
        def mergeSort(arr):
            r=len(arr)
            l=0
            m=r//2
            if r<=1:
                return
            left=arr[:m]
            right=arr[m:]
            mergeSort(left)
            mergeSort(right)
            merge(arr,left,right)
        
        def merge(arr,left,right):
            i,l,r=0,0,0
            while l<len(left) and r<len(right):
                if left[l]<right[r]:
                    arr[i]=left[l]
                    l+=1
                else:
                    arr[i]=right[r]
                    r+=1
                i+=1
            
            while l<len(left):
                arr[i]=left[l]
                l+=1
                i+=1
            
            while r<len(right):
                arr[i]=right[r]
                r+=1
                i+=1

        mergeSort(nums)
        return nums
            