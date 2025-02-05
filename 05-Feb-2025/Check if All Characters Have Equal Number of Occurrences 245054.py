# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter=Counter(s)
        sample=counter[s[0]]

        for i in counter:
            if counter[i]!=sample:
                return False
        return True