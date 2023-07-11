# https://practice.geeksforgeeks.org/problems/subset-sums2234/1

class Solution:
    def subsetSums(self, arr, N):
        
        # code here
        
        lst=[0]
        self.shivesh(arr,0,lst)
        return lst
        
    def shivesh(self,arr,res,lst):
        if not arr:
            return
        
        for i in range(len(arr)):
            lst.append(res+arr[i])
            self.shivesh(arr[i+1:],res+arr[i],lst)