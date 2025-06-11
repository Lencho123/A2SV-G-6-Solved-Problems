# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class UnionFind:
    def __init__(self,n):
        self.s_alice = [1 for i in range(n)]
        self.s_bob = [1 for i in range(n)]
        self.p_alice = [i for i in range(n)]
        self.p_bob = [i for i in range(n)]

    def find(self, alice,bob, x):
        if alice:
            if x == self.p_alice[x]:
                return x
            self.p_alice[x] = self.find(alice,bob, self.p_alice[x])
            return self.p_alice[x]
        else:
            if x == self.p_bob[x]:
                return x
            self.p_bob[x] = self.find(alice,bob, self.p_bob[x])
            return self.p_bob[x]

    def union(self,alice, bob, x, y):
        if alice:
            xp = self.find(True, False, x)
            yp = self.find(True, False, y)

            if xp != yp:
                if self.s_alice[xp] > self.s_alice[yp]:
                    self.p_alice[yp] = xp
                    self.s_alice[xp]+=self.s_alice[yp]
                else:
                    self.p_alice[xp] = yp
                    self.s_alice[yp]+=self.s_alice[xp]
        else:
            xp = self.find(False, True, x)
            yp = self.find(False, True, y)

            if xp != yp:
                if self.s_bob[xp] > self.s_bob[yp]:
                    self.p_bob[yp] = xp
                    self.s_bob[xp]+=self.s_bob[yp]
                else:
                    self.p_bob[xp] = yp
                    self.s_bob[yp]+=self.s_bob[xp]


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        edges.sort(reverse = True)
        res = 0

        for t,u,v in edges:
            u-=1
            v-=1
            if t == 3:
                boool = True
                if uf.find(True,False,u) != uf.find(True,False,v):
                    uf.union(True,False,u,v)
                    boool = False
                if uf.find(False,True,u) != uf.find(False,True,v):
                    uf.union(False,True,u,v)
                    boool = False
                if boool:
                    res+=1
            elif t == 2 and uf.find(False,True,u) != uf.find(False,True,v):
                uf.union(False,True,u,v)
            elif t == 1 and uf.find(True,False,u) != uf.find(True,False,v):
                uf.union(True,False,u,v)
            else:
                res+=1

        for i in range(1,n):
            if uf.find(True,False,i) != uf.find(True,False,i-1) or uf.find(False,True, i) != uf.find(False,True, i-1):
                return -1
        return res