# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def reverser(arr):
            l=0
            r=len(arr)-1
            while l<r:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1

        r=len(arr)
        res=[]
        while r>0:
            seek=0
            mx=0
            while seek<r:
                if arr[seek]>arr[mx]:
                    mx=seek
                seek+=1
            res.append(mx+1)
            res.append(r)

            le=0
            ri=mx
            while le < ri:
                arr[le],arr[ri]=arr[ri],arr[le]
                le+=1
                ri-=1

            le=0
            ri=r-1
            while le < ri:
                arr[le],arr[ri]=arr[ri],arr[le]
                le+=1
                ri-=1
            r-=1

        return res
