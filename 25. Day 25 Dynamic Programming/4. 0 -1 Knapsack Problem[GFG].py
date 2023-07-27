# https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        dp={}
        def solve(n,cap):
            if n==0 or cap==0:
                return 0
            elif (n,cap) in dp:
                return dp[(n,cap)]
                
            else:
                cwt=wt[n-1]
                cv=val[n-1]
                if cwt<=cap:
                    c1=cv+solve(n-1,cap-cwt)
                    c2=solve(n-1,cap)
                    c= max(c1,c2)
                else:
                   c= solve(n-1,cap)
                dp[(n,cap)]=c
                return c
        return solve(n,W)