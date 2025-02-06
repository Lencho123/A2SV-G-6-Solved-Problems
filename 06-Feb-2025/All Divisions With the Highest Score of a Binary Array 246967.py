# Problem: All Divisions With the Highest Score of a Binary Array - https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        l=len(nums)
        leftZero=[0 for i in range(l)]
        rightOne=[0 for i in range(l)]

        runZero=0
        for i in range(l):
            leftZero[i]=runZero
            if nums[i]==0:
                runZero+=1
        
        leftZero.append(runZero)

        # for right
        runOne=0
        for i in range(l):
            rightOne[-1*(i+1)]=runOne
            if nums[-1*(i+1)]==1:
                runOne+=1
        rightOne.insert(0,runOne)

        summ=[]
        for i in range(l+1):
            summ.append(leftZero[i]+rightOne[i])
        
        mx=max(summ)
        
        res=[]
        for i in range(l+1):
            if summ[i]==mx:
                res.append(i)

        return res
        