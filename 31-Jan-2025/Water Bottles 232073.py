# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        left_empty=0
        full=numBottles
        empty=0
        count=0

        while full>0:
            # drink and collect empty
            count+=full
            empty=left_empty+full

            # change empty to full from market
            full=empty // numExchange
            left_empty=empty % numExchange
        return count