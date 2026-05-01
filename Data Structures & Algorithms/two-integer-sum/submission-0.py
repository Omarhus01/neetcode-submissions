class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        n = len(nums)

        for i in range(n):
            reminder = target - nums[i]

            if reminder in seen:
                return [seen[reminder], i]
            print(seen)
            seen[nums[i]] = i
            
