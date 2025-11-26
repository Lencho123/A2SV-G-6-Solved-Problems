# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

def solve():
  n,k = [int(i) for i in input().split()]
  heights = [int(i) for i in input().split()]
  
  dp = [0]*n
  
  for i in range(n-2,-1,-1):
    min_cost = float("inf")
    for j in range(1, k+1):
      if i + j < n:
          min_cost = min(min_cost, abs(heights[i] - heights[i+j]) + dp[i+j])
  
    dp[i] = min_cost
      
  return dp[0]
  
print(solve())