# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        index = 1
        
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                continue
            nums[index] = nums[i]
            index+=1
            
        return index
        
        