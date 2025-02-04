# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

from collections import Counter
q=int(input())

for _ in range(q):
    s=input()
    t=input()
    p=input()
    
    # check order
    def Inorder(s,t):
        sp=0
        tp=0
        
        while sp<len(s) and tp<len(t):
            while tp<len(t) and s[sp]!=t[tp]:
                tp+=1
            
            sp+=1
            tp+=1
        
        if sp==len(s) and tp<=len(t) and s[sp-1]==t[tp-1]:
            return True
        
        return False
    
    # check compensate frequency from p 
    
    def freqChecker(s,t):
        cs=Counter(s)
        ct=Counter(t)
        cp=Counter(p)
        needed=Counter()
        
        for i in ct:
            needed[i]=ct[i]-cs[i]
      
        for j in needed:
            if needed[j]>cp[j]:
                return False
          
        return True
    
    order=Inorder(s,t)
    freq=freqChecker(s,t)
    
    if order and freq:
        print("YES")
    else:
        print("NO")
            

