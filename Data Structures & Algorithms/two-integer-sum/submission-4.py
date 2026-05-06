class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        n = len(nums)

        for i in range(n):
            left = target - nums[i] #i'm guranteed to see the value if I can find it later 

            if left in seen:
                return [seen[left], i]
            
            seen[nums[i]] = i # i = 0 , nums[i] = 3, so I'm saying seen[3] -> {3: 0}
            
            #i = 1 , nums[i]= 4 , left = 3
            #  if 3 in seen, it is : then 
            # give me seen[3] look up key of 3 and get me the value -> 0 (from line13) 
            # and give me the i we are at now (1)
            # the result is [0,1]


      






