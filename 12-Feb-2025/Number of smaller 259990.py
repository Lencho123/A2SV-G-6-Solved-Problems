# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n,m=[int(i) for i in input().split()]

a1=[int(i) for i in input().split()]
a2=[int(i) for i in input().split()]

i=0
res=[]
count=0
for p in range(m):
    while i<n and a1[i]<a2[p]:
        count+=1
        i+=1
    res.append(count)
    p+=1

print(*res)