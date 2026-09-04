class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        seen = {}


        for i in range(n):
            reminder = target - nums[i]

            if reminder in seen:
                return [seen[reminder], i]
            seen[nums[i]] = i
       

