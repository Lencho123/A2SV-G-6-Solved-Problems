# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

def solve(input):
  if len(input) < 2:
    return 0
  dp = [0]*len(input)
  dp[1] = abs(input[0]-input[1])
  
  for i in range(2,len(input)):
    dp[i] = min(dp[i-1]+abs(input[i]-input[i-1]), dp[i-2]+abs(input[i]-input[i-2]))
  return dp[-1]
  
n = int(input())

inputs = [int(i) for i in input().split()]
  
print(solve(inputs))