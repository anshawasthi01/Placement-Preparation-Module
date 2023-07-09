# https://leetcode.com/problems/max-consecutive-ones/description/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        count = 0
        for i in range(len(nums)):
            if nums[i]:
                count+=1
            else:
                ans = max(ans, count)
                count = 0 
                
        ans = max(ans, count)
        return ans

        