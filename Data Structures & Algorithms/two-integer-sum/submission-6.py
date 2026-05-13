class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = {}

        for i in range(n):
            left = target - nums[i]

            if left in seen:
                return [seen[left], i]
            seen[nums[i]] = i 
                
       
      






