class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)

        for i in range(n):
            product = 1
            for j in range(n):
                if i == j:
                    continue
                product *= nums[j]
            res.append(product)
        return res