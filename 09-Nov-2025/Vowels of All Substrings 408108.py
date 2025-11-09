# Problem: Vowels of All Substrings - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        vowels = "aeiou"
        n,res = len(word),0
        for i, char in enumerate(word):
            if char in vowels:
                res += (i+1)*(n-i)

        return res