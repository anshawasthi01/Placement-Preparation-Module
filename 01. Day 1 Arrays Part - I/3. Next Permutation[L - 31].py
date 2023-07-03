# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        for i in range(n-1,0,-1):
            if nums[i] > nums[i-1]:
                
                # find the smallest greater num on right side
                min_ele_idx = 0
                for j in range(i,n):
                    if nums[j] > nums[i-1]:
                        min_ele_idx = j
                        
                        
                # swap the elements
                nums[i-1], nums[min_ele_idx] = nums[min_ele_idx], nums[i-1]
                
                #reverse string starting from i
                left = i
                right = n-1
                while left<right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left+=1
                    right-=1
                return nums
        nums.reverse()
     
                
    
    