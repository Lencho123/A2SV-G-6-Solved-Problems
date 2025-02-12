# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max_area=0

        while l < r:
            max_area=max(max_area, (r-l)*min(height[l],height[r]))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        
        return max_area
