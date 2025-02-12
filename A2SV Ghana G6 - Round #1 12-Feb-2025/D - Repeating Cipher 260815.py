# Problem: D - Repeating Cipher - https://codeforces.com/gym/585132/problem/D

n=int(input())
t=input()

dycrpted=''
pt=0
inc=1

while pt<n:
    dycrpted+=t[pt]
    pt+=inc
    inc+=1

print(dycrpted)