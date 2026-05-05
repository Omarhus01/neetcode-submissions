class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Plan:
        We need to make it now in O(n) instead of n^2, so the thing we can do is use the prefix product
        or prefix/piostfix in other words. We can simply work on tham tby having our input array and then for each 
        element we calculate  the prefix product for it (same as what we did in prtefix sum) and add 
        the values in the results output array 
        and then the plan it like this:
        1) we initialize thep pre /post multipliers with 1 (multuplication identity) 
        2) the beginning and en hav nothing to multiply with , for beginnning wre will work 
        with the prefix vlaue we have curently and append it in the reults array we have
        then we need to update the results by multiplying the current element now with  the value it has 
        so we have  a new prefix for the upcoming elements
        repeating this should fill the output array for all the prefuix queries for each element 
        post fix:
        now for this one , we need to update the results array without overriding it
        so the plan is:
        1) update the results array by multiplying it with the post fix 
        2) I forgot hthat this is the 2nd pass and it's from right ( end ) to left (beginning) 
        3) we then update the post fix after this unlike the preefix one 

        """

        prefix = 1 
        postfix = 1 
        n = len(nums)

        res = [1] * n 

        #1st pass 
        for i in range(n):
            res[i] = prefix # so this what we intialize it with handling first cases here we have 
            #the very fisrt element we knew it will be 1cause we haven't inittialized the 
            # 1st element , we will after updating it (prefix od nums[0] should eb nothign )
            # there is nothign before it 
            prefix *= nums[i] #now we have the new prefix to work with for the upcoming values

        
        #2nd pass
        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

