# Problem: People are leaving - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    class UniounFind:
        def __init__(self,n):
            self.parent=[i for i in range(n+1)]
            self.size=[1 for i in range(n+1)]

        def find(self, x):
            if self.parent[x] == x:
                return x
            self.parent[x] = self.find(self.parent[x])
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
            

    n,m = [int(i) for i in input().split()]
    uf = UniounFind(n)

    for i in range(m):
        op,x = input().split()

        if op == '-':
            uf.parent[int(x)-1] = uf.find(int(x))
        else:
            res = uf.find(int(x)-1)
            if res == n:
                print(-1)
            else:
                print(res+1)
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
