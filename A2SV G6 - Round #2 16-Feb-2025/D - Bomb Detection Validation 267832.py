# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

n,m=[int(i) for i in input().split()]

arr=[]
for i in range(n):
    row=list(input())
    arr.append(row)

flag=True
for i in range(n):
    for j in range(m):
        t,tl,tr,l,r,b,bl,br=0,0,0,0,0,0,0,0
        # t
        if i>0 and arr[i-1][j]=='*':
            t=1
        # tl
        if i>0 and j>0 and arr[i-1][j-1]=="*":
            tl=1
        # tr
        if i>0 and j<m-1 and arr[i-1][j+1]=="*":
            tr=1
        # l
        if j>0 and arr[i][j-1]=="*":
            l=1
        # r
        if j<m-1 and arr[i][j+1]=="*":
            r=1
        # b
        if i<n-1 and arr[i+1][j]=="*":
            b=1
        # bl
        if i<n-1 and j>0 and arr[i+1][j-1]=="*":
            bl=1
        # br
        if i<n-1 and j<m-1 and arr[i+1][j+1]=="*":
            br=1
            
        valid=l+r+tr+tl+t+b+bl+br
        if arr[i][j].isdigit() or arr[i][j]=='.':
            val=0
            if arr[i][j].isdigit():
                val=int(arr[i][j])
                
            if val!=valid:
                flag=False
                print("NO")
                break
                
    if not flag:
        break
if flag:
    print("YES")

    