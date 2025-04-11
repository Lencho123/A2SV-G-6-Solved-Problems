# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        civil = set()
        count = defaultdict(int)
        for c,d in trust:
            civil.add(c)
            count[d]+=1
        
        for i in range(1, n+1):
            if i not in civil and count[i] == n-1:
                return i

        return -1