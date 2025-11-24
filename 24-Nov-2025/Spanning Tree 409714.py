# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

class UnionFind:
    def __init__(self,n):
        self.parent = {i+1:i+1 for i in range(n)}
        self.size = {i+1:1 for i in range(n)}

    def find(self,x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        xp,yp = self.find(x),self.find(y)
        if xp == yp:
            return
        
        if self.size[xp] < self.size[yp]:
            xp,yp = yp,xp
        
        self.parent[yp] = xp
        self.size[xp]+=self.parent[yp]

# I USE KRUSKALS ALGORITHM
n,m = [int(i) for i in input().split()]
weigh_edges = []
for i in range(m):
    u,v,w = [int(i) for i in input().split()]
    weigh_edges.append([w,u,v])

weigh_edges.sort()
uf = UnionFind(n)

min_spining_weigh = 0
for w,u,v in weigh_edges:
    if uf.find(u) != uf.find(v):
        uf.union(u,v)
        min_spining_weigh+=w
print(min_spining_weigh)