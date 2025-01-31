# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha='qwertyuiopasdfghjklzxcvbnm1234567890'
        s=s.lower()

        ns=''
        for i in s:
            if i in alpha:
                ns+=i

        return ns==ns[::-1]
        