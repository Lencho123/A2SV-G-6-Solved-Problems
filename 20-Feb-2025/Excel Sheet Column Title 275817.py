# Problem: Excel Sheet Column Title - https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        orders = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        while columnNumber > 0:
            result += orders[columnNumber % 26 - 1]
            columnNumber = (columnNumber - 1) // 26
    
        return result[::-1]