class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
        plan:
        we need to get the indices of the numbers , w=so the best way is to look in range of the array not 
        the array itself. the easiest way it to subtract the target from each element w eare looping in , 
        then we see , we need to store the numbers somewhere,  ( a dictionary will be good here)
        and from ther  when we get the remider , we can see that if the remider is in this dictionary
        if the dictionary contains the numberdthen we rreturn the inddex of it

        whcih mean
        dict= {the key is the number of the current element we are at nums[i] key: the index is the value}
        plan:
        1) create the dictionary
        2) create a dummy reminder value
        3) check if the value is in our reminder, we reurn the stored value and the curent one we are at now 

        """
        seen = {}
        n = len(nums)

        for i in range(n):
            reminder  = target - nums[i]

            if reminder in seen:
                return [seen[reminder], i]
            
            seen[nums[i]] = i








