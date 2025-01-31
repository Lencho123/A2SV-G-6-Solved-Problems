# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alpha='abcdefghijklmnopqrstuvwxyz'

        count={}
        #convert
        ns=''
        for i,val in enumerate(alpha):
            if val in s:
                count[val]=i+1
        for i in s:
            ns+=str(count[i])


        def transform(ns):
            news=0
            for i in ns:
                news+=int(i)
            return str(news)
        for i in range(k):
            ns=transform(ns)

        return int(ns)