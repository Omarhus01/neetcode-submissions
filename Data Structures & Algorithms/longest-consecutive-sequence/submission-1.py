class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """\
        the pan is simple :

        we make a set of values and then a dummy (longest= 0)
        then we loop across the emenet sin our set 
        if the difference bwewteen num we have - 1is not in ou rset:\
        rhen we add it normally in the set and assume it's outr start point 
        and then we intilize a count variable for it 

        then the tricky part is what we need noew 
        we need a nothe loop that whilee the new num we are at + the current count ()
        s(since they are stacking now) is in the set ( 1+1 = 2 and 2 in our sett , so we increase the count )
        and we keep doing that till we are done , 
        thenn we updae our  dummy with the maximum value between its new longest or the count if it's bigger 
    
        """
        longest = 0 

        seen = set(nums)

        for num in seen:
            if num - 1 not in seen:
                count = 1
                while num + count in seen:
                    count += 1
                longest = max(longest, count)
        return longest     