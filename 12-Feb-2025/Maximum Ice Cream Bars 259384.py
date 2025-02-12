# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        mx=max(costs)

        count=[0 for i in range(mx+1)]
        for i in costs:
            count[i]=count[i]+1
        
        res=0
        price=0
        for i in range(mx+1):
            if count[i]>0:
                for j in range(count[i]):
                    price+=i
                    if price>coins:
                        break
                    res+=1
        return res

        