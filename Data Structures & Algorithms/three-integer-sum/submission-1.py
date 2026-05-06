class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        PLAN

        Sort the array first. Sortedness gives us two big things:
        - We can prune (stop early when smallest pivot is positive).
        - We can use two pointers in the inner loop.
        - Equal values become adjacent, which makes deduplication straightforward.

        Outer loop — pick a pivot index i:
        Walk i from 0 to n-1. nums[i] is the "anchor" of each triplet.

        Two checks before doing work for this i:

        Check 1 — early exit (prune):
            If nums[i] > 0, the smallest element in our pivot+two-pointer search is already 
            positive. The other two values are at indices > i and are at least as large as 
            nums[i], so they're also positive. Three positives can never sum to 0. Break.

        Check 2 — skip duplicate pivot:
            If i > 0 AND nums[i] == nums[i-1], we already explored every triplet starting 
            with this value. Reusing it would generate duplicate triplets. Continue to next i.
            Guard with i > 0 because nums[-1] is the last element, not "nothing."

        Inner loop — two pointers:
        Initialize l = i+1, r = n-1. Walk them inward while l < r.
        Compute total = nums[i] + nums[l] + nums[r].

        Three cases:

        total == 0: found a triplet.
            Step 1: append [nums[i], nums[l], nums[r]] to res.
            Step 2: move BOTH pointers inward (l += 1, r -= 1). This is required for 
                    progress — without it, the same triplet gets found forever.
            Step 3: skip duplicates on both sides:
                    while l < r and nums[l] == nums[l-1]: l += 1
                    while l < r and nums[r] == nums[r+1]: r -= 1
                    This avoids generating the same triplet from a different position.
                    Comparison is l vs l-1 (and r vs r+1) because after step 2, l-1 holds
                    the value we just used.

        total < 0: sum is too small. The right side is already as large as possible for
                    this l, so we need a larger left value. l += 1.

        total > 0: sum is too big. The left side is already as small as possible for
                    this r, so we need a smaller right value. r -= 1.

        Return res.

        Complexity:
        Time: O(n log n) sort + O(n²) for the nested two-pointer scan = O(n²).
        Space: O(1) extra (output array doesn't count). Sort may use O(log n) stack.

        Why this beats brute force O(n³): for each pivot, two pointers scan in linear time 
        instead of nested O(n²). Sortedness is what unlocks this.
        """
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

    



        