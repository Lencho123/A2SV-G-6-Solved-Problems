# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class UnionFInd:
    def __init__(self,n, variables):
        self.parent = {a:a for a in variables}
        self.rank = {a:0 for a in variables}

    def find(self,x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        xp = self.find(x)
        yp = self.find(y)

        if xp != yp:
            if self.rank[xp] > self.rank[yp]:
                self.parent[yp] = xp
            elif self.rank[yp] > self.rank[xp]:
                self.parent[xp] = yp
            else:
                self.parent[yp] = xp
                self.rank[xp]+=1
            

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        variables = set()
        for eqn in equations:
            a = eqn[0]
            b = eqn[-1]

            variables.add(a)
            variables.add(b)
        
        variables = list(variables)
        uf = UnionFInd(len(variables),variables)

        for eq in equations:
            if eq[1:3] == '==':
                uf.union(eq[0],eq[-1])
                
        for eq in equations:
            if eq[1:3] == '!=' and uf.find(eq[0]) == uf.find(eq[-1]):
                return False
        return True
                