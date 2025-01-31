# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # first identify the pellow mov't direction
        direction=ceil(time/(n-1))
        
        # to right
        if direction%2==1:
            if time % (n-1)==0:
                return n
            else:
                return time % (n-1) + 1
        else:
            if time % (n-1)==0:
                return 1
            else:
                return n - time % (n-1) 