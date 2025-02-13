# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        mx_len=0
        mx_freq=0
        count=defaultdict(int)

        for r in range(len(s)):
            count[s[r]]+=1
            mx_freq=max(count[s[r]], mx_freq)

            while (r-l+1)-mx_freq > k:
                count[s[l]]-=1
                l+=1

            mx_len=max(mx_len, r-l+1)

        return mx_len
