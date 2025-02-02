# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:  
        num=[str(n) for n in digits]
        num=int(''.join(num))+1
        num=str(num)

        return list(map(int, num))
        