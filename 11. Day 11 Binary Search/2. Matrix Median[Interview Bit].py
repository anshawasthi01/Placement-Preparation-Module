# https://www.interviewbit.com/problems/matrix-median/

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        l = []
        for  i in A:
            l.extend(i)
        ln = len(l)
        l.sort()
        if ln % 2 !=0:
            return l[ln//2]
        else:
            return (l[n//2]+l[n//2-1])//2