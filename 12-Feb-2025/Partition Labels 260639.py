# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        yeah_right=0
        counter=Counter(s)
        encountered=set()
        res=[]
        left=0

        for i in range(len(s)):
            if s[i] not in encountered:
                yeah_right+=1

            encountered.add(s[i])
            
            counter[s[i]]-=1
            if counter[s[i]]==0:
                yeah_right-=1
            
            if yeah_right==0:
                res.append((i+1)-left)
                left=i+1

        return res