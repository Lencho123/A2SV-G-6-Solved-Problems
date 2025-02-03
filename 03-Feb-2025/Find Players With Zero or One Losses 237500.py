# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost_count=defaultdict(int)
        winner_count=defaultdict(int)

        for i in matches:
            lost_count[i[1]]+=1
            winner_count[i[0]]+=1

        noLost=[]
        oneLost=[]

        for play in lost_count:
            if lost_count[play]==1:
                oneLost.append(play)
        for win in winner_count:
            if win not in lost_count:
                noLost.append(win)

        noLost.sort()
        oneLost.sort()
        return [noLost, oneLost]
        

