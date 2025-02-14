# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def isValid(window, tc):
            for char in tc:
                if window[char] < tc[char]:
                    return False
            return True
            
        left=0
        res=s+'a'
        tc=Counter(t)
        window=defaultdict(int)

        for right in range(len(s)):
            window[s[right]]+=1
            # check windows validity
            while isValid(window,tc):
                if len(res)>right-left+1:
                    res=s[left:right+1]
                window[s[left]]-=1
                left+=1
            # print(window)
        return res if len(res) <= len(s) else ''
        