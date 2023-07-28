# https://practice.geeksforgeeks.org/problems/palindromic-patitioning4845/1

class Solution:
    def palindromicPartition(self, string):
        # code here
        n = len(string)
        
        t = [[-1]*(n+1) for _ in range(n+1)]
        
        def isPalindrome(st):
            return st == st[::-1]
            
            
        def solve(i, j):
            if i >= j:
                return 0
                
            if t[i][j] != -1:
                return t[i][j]
                
            if isPalindrome(string[i:j+1]):
                return 0
                
                
            res = float('inf')
            for k in range(i, j):
                # we have to make partitions such that each substring is a palindrome
                # hence we will only move further if the first parttion is palindrome
                # if the first part is not a palindrome that means this is not a valid solution 
                # and hence we will not check for the second part
                if isPalindrome(string[i:k+1]):
                    temp = solve(k+1, j) + 1
                    res = min(res, temp)
                
            t[i][j] = res
            return t[i][j]
            
        return solve(0, n-1)