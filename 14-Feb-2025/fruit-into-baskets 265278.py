# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        counter=defaultdict(int)
        res=0

        for right in range(len(fruits)):
            counter[fruits[right]]+=1

            while len(counter)>2:
                counter[fruits[left]]-=1
                if counter[fruits[left]]==0:
                    counter.pop(fruits[left])
                left+=1
            
            res=max(res, right-left+1)
        
        return res