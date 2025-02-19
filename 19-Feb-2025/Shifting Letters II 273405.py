# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        alpha='abcdefghijklmnopqrstuvwxyz'
        index=defaultdict(int)
        for i in range(len(alpha)):
            index[alpha[i]]=i

        pre=[0 for i in range(len(s)+1)]
        for shift in shifts:
            l,r,d = shift
            if d==1:
                pre[l]+=1
                pre[r+1]-=1
            else:
                pre[l]-=1
                pre[r+1]+=1
        
        for i in range(1,len(pre)):
            pre[i]=pre[i]+pre[i-1]

        res=''
        for i in range(len(s)):
            if pre[i]>=0:
                ind=(index[s[i]]+pre[i])%26
                res+=alpha[ind]
            else:
                indp=abs(pre[i])%26
                ind=index[s[i]]-indp
                res+=alpha[ind]

        return res