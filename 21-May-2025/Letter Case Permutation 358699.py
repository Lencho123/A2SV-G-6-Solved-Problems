# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = (1<<len(s))
        l = len(s)
        visited = set()
        visited.add(s)

        res = [s]

        for i in range(n):
            change_occur = False
            cand = list(s)

            for k in range(l):
                if i & (1<<k) != 0 and not s[-k-1].isdigit():
                    cand[-k-1] = s[-k-1].swapcase()
                    change_occur = True

            cur = ''.join(cand)
            if change_occur and cur not in visited:
                res.append(cur)
                visited.add(cur)

        return res