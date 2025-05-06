# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class UnionFind:
    def __init__(self, n):
        self.rank = [0 for i in range(n)]
        self.parent = [i for i in range(n)]

    def union(self,x,y):
        x_p = self.find(x)
        y_p = self.find(y)

        if x_p != y_p:
            if self.rank[x_p] == self.rank[y_p]:
                self.parent[y_p] = x_p
                self.rank[x_p]+=1
            elif self.rank[x_p] > self.rank[y_p]:
                self.parent[y_p] = x_p
            else:
                self.parent[x_p] = y_p
            return False
        else:
            return True

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        Uf = UnionFind(len(edges))

        for u,v in edges:
            u,v = u-1,v-1

            if Uf.union(u,v):
                return [u+1,v+1]