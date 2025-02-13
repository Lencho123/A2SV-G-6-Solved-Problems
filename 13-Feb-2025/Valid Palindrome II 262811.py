# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValid(s):
            l=0
            r=len(s)-1
            while l < r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True

        l=0
        r=len(s)-1

        while l<r:
            if s[l]!=s[r]:
                break
            l+=1
            r-=1
        # check validity by removing s[l]
        left_s=s[:l]+s[l+1:]
        right_s=s[:r]+s[r+1:]

        return True if isValid(left_s) or isValid(right_s) else False