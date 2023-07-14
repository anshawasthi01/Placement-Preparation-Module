# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []
        for el in nums:
            if len(hp)<k:
                heapq.heappush(hp, el)

            else:
                if hp[0]<el:
                    heapq.heappush(hp, el)
                    heapq.heappop(hp)
        return hp[0]                    