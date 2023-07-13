# https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        i=0
        j=0
        count=1
        while i<n and j<m:
            if arr1[i]<=arr2[j]:
                temp=arr1[i]
                i+=1
            else:
                temp=arr2[j]
                j+=1
            if count==k:
                return temp
            count+=1
        while i<n:
            temp=arr1[i]
            i+=1
            if count==k:
                return temp
            count+=1
        while j<m:
            temp=arr2[j]
            j+=1
            if count==k:
                return temp
            count+=1