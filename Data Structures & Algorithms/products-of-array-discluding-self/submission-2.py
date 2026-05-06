class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        we can have the identity (1) and then use it for prefix and post fix adn 

        then we can use them to or n the operationed and we have the output array
        sowhatever is before i , we multipuy it with the prefix and then upadte the outpout array 
        this gives us all the vlaues before the i in the out put array 
        for the pos fix we will work form the rerverse order and fill the rest of th eoutsput array 
        so since output array is alrready filled , we need to update it first an then uupdate the post fix unlike 
        the prefix where these steps weere swapped\
        we assign first for pre , then updaate 
        for pot 
        we update first then we assign 
        """
        pre = 1 
        post = 1
        n = len(nums)
        res = [1] * n
        for i in range(n):
            res[i] = pre 
            pre *= nums[i]

        for i in range(n-1, -1, -1 ):
            res[i] *= post 
            post *= nums[i]

        return res

       

