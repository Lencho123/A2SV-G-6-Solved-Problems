# Problem: Length of Last Word - https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # last,start=0,0
        # for i in range(len(s)-1, -1,-1):
        #     if s[i]!=' ':
        #         last=i
        #         break
        # for j in range(last, -1,-1):
        #     if s[j]==' ':
        #         start=j+1
        #         break
        # print(last,start)
        # return last-start+1
        
        last=len(s)-1
        while s[last]==' ':
            last-=1
        
        start=last
        while start>0 and s[start]!=' ':
            start-=1
        

        word= s[start:last+1] if s[start]!=' ' else s[start+1:last+1]
        return len(word)