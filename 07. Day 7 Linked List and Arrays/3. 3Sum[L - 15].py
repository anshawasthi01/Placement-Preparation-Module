# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i,a in enumerate(nums):
            if(i>0 and a==nums[i-1]):
                #for duplicate of the first position...
                continue
            l,r=i+1,len(nums)-1
            while(l<r):
                three=a+nums[l]+nums[r]
                if(three>0):
                    r-=1
                elif(three<0):
                    l+=1
                else:
                    p=[]
                    p.append(a)
                    p.append(nums[l])
                    p.append(nums[r])
                    res.append(p)
                    while nums[l]==p[1]  and l<r :
                        #second point duplicates...
                        l+=1
                    while nums[r]==p[2] and l<r:
                        #third point duplicactes...
                        r-=1
        return res
                
            