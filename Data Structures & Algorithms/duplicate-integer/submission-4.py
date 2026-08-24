class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        here = set()

        for num in nums:
            if num in here:
                return True
            here.add(num)
        return False