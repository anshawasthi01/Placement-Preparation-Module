# https://www.interviewbit.com/problems/nearest-smaller-element/

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        ans = []
        stack = []
        for i in range(0, len(A), 1): 
            while (stack!=[] and stack[-1]>=A[i]):
                stack.pop()
            if stack == []:
                ans.append(-1)
            else:
                ans.append(stack[- 1])
            
            stack.append(A[i])
        
        return ans
