# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rechest=sum(accounts[0])

        for i in accounts:
            rechest=max(rechest, sum(i))

        return rechest
        