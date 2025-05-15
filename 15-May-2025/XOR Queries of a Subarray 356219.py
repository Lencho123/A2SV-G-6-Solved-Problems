# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        xor_pref = [0]
        run_xor = 0
        for num in arr:
            run_xor^=num
            xor_pref.append(run_xor)
        
        ans = []
        for l,r in queries:
            ans.append(xor_pref[r+1]^xor_pref[l])
            
        return ans