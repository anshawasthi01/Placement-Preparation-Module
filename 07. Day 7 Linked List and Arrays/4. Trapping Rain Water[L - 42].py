# https://leetcode.com/problems/trapping-rain-water/

# striver
class Solution:
    def trap(self, height: List[int]) -> int:
        n, l, r, w = len(height), 0, len(height)-1, 0
        lmax, rmax = 0, 0

        while l<=r:
            if height[l] <= height[r]:
                if height[l] >= lmax:
                    lmax = height[l]      
                else:
                    w += lmax - height[l]
                l+=1
            else:
                if height[r] >= rmax:
                    rmax = height[r]      
                else:
                    w += rmax - height[r]
                r -= 1
        return w


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n==1:
            return 0
        left = [0]*n
        right = [0]*n 
        water = 0
        left[0] = height[0]

        for i in range( 1, n):
            left[i] = max(left[i-1], height[i])
            right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i + 1], height[i])
        for i in range(0, n):
            water += min(left[i], right[i]) - height[i]
        return water























        # n, l, r, w = len(height), 0, len(height)-1, 0
        # lmax, rmax = 0, 0

        # while l<=r:
        #     lmax = max(lmax, height[l])
        #     rmax = max(rmax, height[r])

        #     if lmax<=rmax:
        #         w = w - height[l] + lmax
        #         lmax += 1
        #     else:
        #         w = w - height[r] + rmax
        #         rmax -= 1  
        # return w              


















