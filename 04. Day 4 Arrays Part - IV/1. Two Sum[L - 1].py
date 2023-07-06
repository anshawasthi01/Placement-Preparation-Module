# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, el1 in enumerate(nums):
            for j, el2 in enumerate(nums):
                if el1+el2==target and i!=j:
                    return [min(i,j),max(i,j)]
                
                
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m={}
        for i, el in enumerate(nums):
             if target-el in m:
                return [m[target-el],i]
             m[el]=i    

                