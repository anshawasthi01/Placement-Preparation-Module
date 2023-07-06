# https://leetcode.com/problems/4sum/description/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        hmap = defaultdict(int)
        n,res=len(nums),[]
        for i in range(0,n):
            if(i>0 and nums[i-1]==nums[i]):
                continue;
            for j in range(i+1,n):
                for k in range(j+1,n):   
                    t = target-(nums[i]+nums[j]+nums[k])
                    idx = bisect.bisect_left(nums[k+1:n],t)
                    if( k+idx+1 < n and nums[k+idx+1]== t ):
                        lis = [nums[i],nums[j],nums[k],nums[k+idx+1]]
                        temp = ''.join(map(str,lis))
                        if(hmap[temp] == 0 ):
                            res.append(lis)
                            hmap[temp] = 1
                    
                    
        print(res)
        return res
        