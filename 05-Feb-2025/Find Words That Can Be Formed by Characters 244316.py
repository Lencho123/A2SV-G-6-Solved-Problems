# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def isPossible(s, count_char):
            count_s=Counter(s)
            for i in count_s:
                if count_s[i]>count_char[i]:
                    return False
            return True

        count=0
        count_char=Counter(chars)
        for s in words:
            if isPossible(s, count_char):
                count+=len(s)

        return count