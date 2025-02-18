# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n,k,q = [int(i) for i in input().split()]

recipes=[]
queries=[]

for i in range(n):
    l,r=[int(i) for i in input().split()]
    recipes.append([l,r])

for i in range(q):
    a,b=[int(i) for i in input().split()]
    queries.append([a,b])

# pre for recipies

pre=[0 for i in range(200002)]
for l,r in recipes:
    pre[l]+=1
    pre[r+1]-=1

for i in range(1,200002):
    pre[i]=pre[i-1]+pre[i]

# construct pre for admmissable recipies

admissable=[0 for i in range(200002)]

for i in range(1,200002):
    if pre[i]>=k:
        admissable[i]=admissable[i-1]+1
    else:
        admissable[i]=admissable[i-1]

for a,b in queries:
    print(admissable[b]-admissable[a-1])
