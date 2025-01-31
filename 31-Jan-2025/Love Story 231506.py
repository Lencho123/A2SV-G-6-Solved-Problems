# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

t=int(input())

for test in range(t):
    word='codeforces'
    s=input()
    count=0
    
    for i in range(10):
        if word[i] != s[i]:
            count+=1
    
    print(count)