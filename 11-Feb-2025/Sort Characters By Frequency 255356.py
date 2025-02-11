# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)
        
        freq=count.values()
        freqFreq=defaultdict(list)
        for i in count:
            freqFreq[count[i]].append(i)

        res=''
        keys=list(freqFreq.keys())
        keys.sort(reverse=True)
        for i in keys:
            for char in freqFreq[i]:
                res+=char*i
        return res