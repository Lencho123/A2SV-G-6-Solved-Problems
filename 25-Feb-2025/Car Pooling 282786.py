# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pre=[0 for i in range(1001)]

        for pasn,s,e in trips:
            pre[s]+=pasn
            pre[e]-=pasn
        
        curr_passangers=pre[0]
        for i in range(1,1001):
            if curr_passangers > capacity:
                return False
            curr_passangers+=pre[i]
        
        return True