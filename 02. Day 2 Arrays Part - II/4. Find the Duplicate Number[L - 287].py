# https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Positioning Method
        while nums[0] != nums[nums[0]]:
            nums[0], nums[nums[0]] = nums[nums[0]], nums[0]
        return nums[0]