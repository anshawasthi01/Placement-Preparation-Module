# https://leetcode.com/problems/powx-n/description/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        #Base
        if n==0:
            return 1.000    
        
        #flags
        isxneg, isnneg = x<0, n<0
        x, n = abs(x), abs(n)
        
           
        #if n==1:
        #   return 1/x if isnneg else x
        
        
        #original algo
        halfans = self.myPow(x, n//2)
        if n%2 == 1:
            ans = halfans*halfans*x
        else:
            ans=halfans*halfans
            
        # flag checks
        if isxneg and n%2 == 1:
            ans = -ans
        if isnneg :
            ans = 1/ans
        return ans
            
        
        