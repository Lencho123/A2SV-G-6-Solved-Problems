# Problem: Sum - https://codeforces.com/contest/1742/problem/A

t=int(input())

for test in range(t):
    a,b,c=[int(num) for num in input().split()]
    flag=True

    for i in range(3):
        if a+b==c or a+c==b or b+c==a:
            print("YES")
            flag=False
            break

    if flag:
        print("NO")