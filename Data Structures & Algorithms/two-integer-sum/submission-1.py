class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1) we need to have a dictionary that holds the indices of the vlaues
        we saw in the array , 
        2) th easiest way to do this is by having the indices are the values to work on 
        so in this case we need the key to be the values in arrays
        and the indices are the values inthe dictionary 
        {3: 0, 4:1, 5:2, 6:3}
        and from there we can look it faster since the whoel point fo the dictionary is 
        to look uup 
        the issue is how you access the values 
        so we build the dictionary in this way 
        we have a place holder for the complement of the vlues that get our target
        once we find the compement inthe dictionary , we return it and the curretn value we are 
        stopping at 
        since we loop on indeces we need range not normal looping 
        """
        seen = {}
        n = len(nums)

        # now we set the loop and the and get the reminder
        for i in range(n):
            reminder = target - nums[i] #   4 = 7 -3, 3 = 7 -4

            #now we need to see if the reminder is in our dictionary

            if reminder in seen: #reminder is 3 
                return [seen[reminder],i] #seen[3] --> 0 , and tghe current one we are at is i --> 1 
            print(seen)
            seen[nums[i]] = i #seen[3] = 0 --> {3: 0} key is value , index is value
            print(seen)