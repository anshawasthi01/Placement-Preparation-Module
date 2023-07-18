https://www.interviewbit.com/problems/minimum-characters-required-to-make-a-string-palindromic/

class Solution:
    # @param A : string
    # @return an integer
    def create_lps(self,A):
        M=len(A)
        lps=[None]*M
        l=0
        lps[0]=l
        i=1
        
        while i<M:
            if A[i]==A[l]:
                l+=1
                lps[i]=l
                i+=1
            else:
                if l!=0:
                    l=lps[l-1]
                else:
                    lps[i]=0
                    i+=1
        return lps
        
        
    def solve(self, A):
        lps=self.create_lps(A+"$"+A[::-1])
        return len(A)-lps[-1]