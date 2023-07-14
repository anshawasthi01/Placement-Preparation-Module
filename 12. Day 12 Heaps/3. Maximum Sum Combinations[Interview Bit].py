# https://www.interviewbit.com/problems/maximum-sum-combinations/

import heapq
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        retriver = MaxSumRetriver(A, B)
        return [retriver() for _ in range(C)]
        
        
class MaxSumRetriver:
    def __init__(self, A, B):
        self.A = sorted(A, reverse = True) 
        self.B = sorted(B, reverse=True)
        self.sums, self.visited = list(), set()
        self.__add_element(0, 0)
        
    def __call__(self):
        el_sum, indexes = heapq.heappop(self.sums)
        iA, iB = indexes
        self.__add_element(iA, iB + 1)
        self.__add_element(iA + 1, iB)
        return -el_sum
        
    def __add_element(self, iA, iB):
        indexes = iA, iB
        if iA < len(self.A) and iB < len(self.B) and indexes not in self.visited:
            heapq.heappush(self.sums, (-self.A[iA] - self.B[iB], indexes))
            self.visited.add(indexes)
    

