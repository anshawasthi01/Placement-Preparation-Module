# https://leetcode.com/problems/top-k-frequent-elements/

import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        hp = []

        for el in freq:
            count = freq[el]
            heapq.heappush(hp, (count,el))

            if len(hp)>k:
                heapq.heappop(hp)

        return [x[1] for x in hp]

