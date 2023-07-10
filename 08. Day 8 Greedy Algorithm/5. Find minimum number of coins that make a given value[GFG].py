# https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/

#User function Template for python3
class Solution:
    def minCoins(self, coins, n, val):
                        
        dp=[[-1]*(val+1)]*(n+1)
        mx = 99999999
        def solve(coins,n,val):
            if val==0:
                return 0
            if n==0:
                return mx
            if dp[n][val]!=-1:
                return dp[n][val]
            if coins[n-1]<=val:
                dp[n][val] = min(1+solve(coins,n,val-coins[n-1]),solve(coins,n-1,val))
                return dp[n][val]
            dp[n][val] =  solve(coins,n-1,val)
            return dp[n][val]
        ans =  solve(coins,n,val)
        if mx == ans:
            return -1
        print(dp)
        return ans