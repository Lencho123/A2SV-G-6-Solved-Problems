# Problem: B - Square String? - https://codeforces.com/gym/585132/problem/B

t = int(input())

for _ in range(t):
    s=input()
    flag=True
    
    for i in range(len(s)):
        if s[:i]==s[i:]:
            print("YES")
            flag=False
            break
    
    if flag:
        print("NO")