class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        count = Counter(nums)
        n = len(nums)
        res = []
        buckets =[[] for _ in range(n+1)] #list comprehension 
        for num, freq in count.items():
            buckets[freq].append(num)
        
       # print(buckets)
        for i  in range(n , 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res 
