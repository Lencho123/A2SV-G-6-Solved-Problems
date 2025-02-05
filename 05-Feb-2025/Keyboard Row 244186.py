# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1="qwertyuiop"
        r2="asdfghjkl"
        r3="zxcvbnm"

        def r1Checker(s,r1):
            for i in s:
                if i not in r1:
                    return False
            return True

        def r2Checker(s,r2):
            for i in s:
                if i not in r2:
                    return False
            return True
            
        def r3Checker(s,r3):
            for i in s:
                if i not in r3:
                    return False
            return True

        res=[]
        for s in words:
            st=s.lower()
            one=r1Checker(st, r1)
            two=r2Checker(st,r2)
            three=r3Checker(st,r3)

            if one or two or three:
                res.append(s)
            
        return res
