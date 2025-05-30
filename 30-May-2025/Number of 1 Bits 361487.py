# Problem: Number of 1 Bits - https://leetcode.com/problems/number-of-1-bits/description/

class Solution:
    def hammingWeight(self, n: int) -> int:
        return(n.bit_count())