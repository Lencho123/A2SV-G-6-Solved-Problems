# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class UnionFind:
    def __init__(self,n):
        self.size = [1 for i in range(n)]
        self.parent = [i for i in range(n)]

    def find(self,x):
        if x == self.parent[x]:
            return x
        self.parent[x]= self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xp = self.find(x)
        yp = self.find(y)

        if xp != yp:
            if self.size[xp] > self.size[yp]:
                self.parent[yp] = xp
                self.size[xp]+=self.size[yp]
            else:
                self.parent[xp] = yp
                self.size[yp]+=self.size[xp]
            

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:

        for i, e in enumerate(edgeList):
            e[0],e[2] = e[2],e[0]

        for j, e in enumerate(queries):
            e[0],e[2] = e[2],e[0]
            e.append(j)
        
        edgeList.sort()
        queries.sort()

        uf = UnionFind(n)

        j = 0
        ans = [False for i in range(len(queries))]
        for i in range(len(queries)):
            # construct unioun with current limit
            while j < len(edgeList) and edgeList[j][0] < queries[i][0]:
                uf.union(edgeList[j][1], edgeList[j][2])
                j+=1
            
            if uf.find(queries[i][1]) == uf.find(queries[i][2]):
                ans[queries[i][3]] = True
        
        return ans


