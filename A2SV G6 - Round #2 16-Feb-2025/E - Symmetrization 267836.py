# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

t=int(input())
for _ in range(t):
    n=int(input())
    arr=[]
    for i in range(n):
        row=input()
        arr.append(list(row))

    operation=0
    
    l=0
    r=n-1
    t=0
    b=n-1
    
    while l<r:
        for i in range(r-l):
            count={'0':0, '1':0}
            
            cell=arr[t][l+i]
            count[cell]+=1
            
            cell=arr[t+i][r]
            count[cell]+=1
            
            cell=arr[b][r-i]
            count[cell]+=1
            
            cell=arr[b-i][l]
            count[cell]+=1
            
            operation+=min(count['0'], count['1'])
        l+=1
        t+=1
        b-=1
        r-=1
    print(operation)