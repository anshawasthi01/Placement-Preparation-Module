# https://practice.geeksforgeeks.org/problems/egg-dropping-puzzle-1587115620/1

class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self,n, k):
        dp = [[0 for _ in range(n+1)]for _ in range(k+1)]
        for i in range(1,k+1):
            for j in range(1,n+1):
                dp[i][j] = 1+dp[i-1][j-1]+dp[i-1][j]
                if dp[i][j]>=k:
                    return i