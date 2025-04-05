# Problem: E - Tv Off - https://codeforces.com/gym/589822/problem/E

n=int(input())
time=[]

for index in range(n):
    l,r = [int(i) for i in input().split()]
    time.append([l,r,index+1])

time.sort(key=lambda x:[x[0],[1]])
flag=True

for i in range(n-1):
    if time[i+1][0] <= time[i][0] <= time[i][1] <= time [i+1][1]:
        print(time[i][2])
        flag = False 
        break
    elif time[i][0] <= time[i+1][0] <= time[i+1][1] <= time[i][1]:
        print(time[i+1][2])
        flag = False
        break
    elif i > 0 and time[i+1][0] <= time[i-1][1]+1:
        merged = [time[i-1][0], time[i+1][1]]
        if merged[0] <= time[i][0] <= time[i][1] <= merged[1]:
            print(time[i][2])
            flag=False
            break

if flag:
    print(-1)