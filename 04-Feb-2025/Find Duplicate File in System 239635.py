# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for p in paths:
            splitted=p.split()
            for j in range(1,len(splitted)):
                deepsplit=splitted[j].split("(")
                key=deepsplit[1][:-1]
                value=deepsplit[0]
	
                d[key].append(splitted[0]+"/"+value)
            
        res=[val for val in d.values() if len(val)>1]

        return res