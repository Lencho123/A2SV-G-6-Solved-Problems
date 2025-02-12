# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a=0
        b=int(c**(1/2))

        while a<=b:
            if a**2 + b**2 == c:
                return True
            
            if a**2 + b**2 < c:
                a+=1
            else:
                b-=1
        
        return False
        