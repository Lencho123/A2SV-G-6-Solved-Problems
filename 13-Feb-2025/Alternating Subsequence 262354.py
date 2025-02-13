# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t=int(input())

for _ in range(t):
    n=int(input())
    arr=[int(i) for i in input().split()]
    
    # Subsequence start with positve
    p=0
    while p < n and arr[p]<0:
        p+=1
    
    pos_sequence=[]
    
    while p < n:
        mxp=float("-inf")
        mxn=float("-inf")
        
        while p < n and arr[p]>0:
            mxp=max(arr[p], mxp)
            p+=1
            
        pos_sequence.append(mxp)
        if p == n:
            break
        
        while p<n and arr[p]<0:
            mxn=max(mxn, arr[p])
            p+=1
        
        pos_sequence.append(mxn)
    # print(pos_sequence)
    
    # Subsequence start with negative
    p=0
    while p < n and arr[p]>0:
        p+=1
    
    neg_sequence=[]
    
    while p < n:
        mxp=float("-inf")
        mxn=float("-inf")
        
        while p<n and arr[p]<0:
            mxn=max(mxn, arr[p])
            p+=1
            
        neg_sequence.append(mxn)
        if p == n:
            break
        
        while p < n and arr[p]>0:
            mxp=max(arr[p], mxp)
            p+=1
        
        neg_sequence.append(mxp)
    
    if len(pos_sequence)>len(neg_sequence):
        print(sum(pos_sequence))
    elif len(pos_sequence)<len(neg_sequence):
        print(sum(neg_sequence))
    else:
        print(max(sum(pos_sequence), sum(neg_sequence)))
         