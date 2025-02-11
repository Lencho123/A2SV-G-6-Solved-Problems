# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)

        n=len(piles)//3
        coin=0

        index=1
        i=0
        while i < n:
            coin+=piles[index]
            index+=2
            i+=1
        return coin