from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        unique= []
        counter = Counter(nums)
        
        for key, value in counter.items():
            heapq.heappush(res, (-value, key))

        while k >0:
            popped = heapq.heappop(res)
            unique.append(popped[1])
            k-= 1
        return unique

        