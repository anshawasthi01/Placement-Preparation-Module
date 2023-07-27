# https://practice.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence4749/1

class Solution:
	def maxSumIS(self, Arr, n):
        msis=[x for x in arr]
            for i in range(1, len(arr)):
                for j in range(i):
                    if(arr[j]<arr[i]):
                        msis[i]=max(msis[i], arr[i]+msis[j])
            return max(msis)
