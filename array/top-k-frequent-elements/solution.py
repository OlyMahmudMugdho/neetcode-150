import heapq
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        print(counter)
        min_heap = []

        for num, freq in counter.items():
            heapq.heappush(min_heap, (freq, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
 
        print(min_heap) 
        return [num for freq, num in min_heap]



s = Solution()
print(s.topKFrequent([1,1,1,2,2,3],2))
