# Problem: Books - https://codeforces.com/contest/279/problem/B

n,t = [int(i) for i in input().split()]
a=[int(i) for i in input().split()]

time=0
left=0
res=0

for right in range(n):
    time+=a[right]
    while time > t:
        time-=a[left]
        left+=1
    
    res= max(res, right-left+1)
print(res)