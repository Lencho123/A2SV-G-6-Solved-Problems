# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n,s=[int(i) for i in input().split()]

a=[int(i) for i in input().split()]

left=0
runsum=0
res=0
for right in range(n):
    runsum+=a[right]
    while runsum > s:
        runsum-=a[left]
        left+=1
    
    res=max(res, right-left+1)

print(res)