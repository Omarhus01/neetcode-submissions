class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            # 1st checker if i > 0 we break
            if nums[i] > 0:
                break
            #2nd checker, if the next offset is repeated, we continue I forgot 
            # that we need to ad dthe i > 0 as well caause if not i-1 = -1 which is worn 
            elif i > 0 and nums[i] == nums[i -1]:
                continue 
            
            #intialization fo the pointers 
            l = i+1 
            r = n - 1

            #inner loop with all of it's cases
            while l < r:
                #get the summation 
                total = nums[i] + nums[l] + nums[r]
                #check if we appedn it or not 
                if total == 0:
                    res.append([nums[i] , nums[l] , nums[r]])
                    l +=1 
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l +=1 
                    #handling r as well in case of repeate elements
                    while l < r and nums[r] == nums[r+1]:
                        r -=1
                elif total < 0:
                    l +=1
                else:
                    r-=1 
        return res



        