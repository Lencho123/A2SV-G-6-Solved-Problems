# Problem: Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

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

n,m,k = [int(i) for i in input().split()]

edges = []
for i in range(m):
    u,v = [int(i) for i in input().split()]

    t = [u,v]
    t.sort()
    edges.append(tuple(t))
# edges_sets = set(edges)

cuts = []
ask_cut = []
for i in range(k):
    op,n1,n2 = [i for i in input().split()]
    n1 = int(n1)
    n2 = int(n2)

    t = [n1,n2]
    t.sort()
    ask_cut.append([op]+t)
    if op == "cut":
        cuts.append(tuple(t))
# ============================= #
cuts.reverse()
ask_cut.reverse()

cut_lookup = set(cuts)

uf = UnionFind(n)
for u,v in edges:
    if (u,v) not in cut_lookup:
        uf.union(u,v)
res = []
for op,u,v in ask_cut:
    if op == "ask":
        if uf.find(u) == uf.find(v):
            res.append("YES")
        else:
            res.append("NO")
    else:
        uf.union(u,v)
res.reverse()
for ans in res:
    print(ans)