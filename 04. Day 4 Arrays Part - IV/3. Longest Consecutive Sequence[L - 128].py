# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        output = 0

        for n in nums:
            if n-1 not in nums:
                start = n
                while start in nums:
                    start+=1

                output = max(output, start-n)
        return output

      