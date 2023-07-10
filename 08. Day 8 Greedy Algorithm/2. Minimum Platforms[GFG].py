# https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1#

#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        platf = 1
        cnt = 1
        i = 1
        j = 0
        while i<n and j<n:
            if arr[i]<=dep[j]: # one more platform needed
                platf+=1
                i+=1
            elif arr[i]>dep[j]:  # one platform can be reduced
                platf-=1
                j+=1
            cnt = max(platf,cnt)
        return cnt