# https://practice.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1

class Solution:
    def matrixMultiplication(self, n, arr):
        # code here
        t = [[-1]*(n+1) for _ in range(n+1)]
        
        def solve(i, j):
            if i >= j:
                return 0
            
            if t[i][j] != -1:
                return t[i][j]
                
            min = float('inf')
            for k in range(i, j):
                temp = solve(i, k) + solve(k+1, j) + arr[i-1]*arr[k]*arr[j]
                
                if temp < min:
                    min = temp
            
            t[i][j] = min
            return t[i][j]
        
        return solve(1, n-1)