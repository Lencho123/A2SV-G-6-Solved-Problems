# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        res=0
        counter={
        "I":             1,
        "V":             5,
        "X":             10,
        "L":             50,
        "C":             100,
        "D":             500,
        "M":             1000}

        l=len(s)
        i=0
        while i<l:
            flag=True
            if i<l-1:
                if s[i]=="I" and s[i+1]=="V":
                    res+=4
                    i+=2
                    flag=False
                elif s[i]=="I" and s[i+1]=="X":
                    res+=9
                    i+=2
                    flag=False
                elif s[i]=="X" and s[i+1]=="L":
                    res+=40
                    i+=2
                    flag=False
                elif s[i]=="X" and s[i+1]=="C":
                    res+=90
                    i+=2
                    flag=False
                elif s[i]=="C" and s[i+1]=="D":
                    res+=400
                    i+=2
                    flag=False
                elif s[i]=="C" and s[i+1]=="M":
                    res+=900
                    i+=2
                    flag=False
                    
            if flag and i<l:
                res+=counter[s[i]]
                i+=1
        return res
        