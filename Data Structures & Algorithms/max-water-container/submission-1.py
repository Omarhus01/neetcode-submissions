class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Two pointers from opposite ends, moving inward.

        Key insight: area = width * min(heights[l], heights[r]).
        The shorter side is the bottleneck. Moving the taller side inward can
        only shrink width while min stays the same or smaller — area can only
        decrease. Moving the shorter side is the only move that might find a
        taller bottleneck and beat the current area.

        So: always move the pointer at the shorter line. Track max along the way.

        Time:  O(n) — pointers cross once, O(1) per step.
        Space: O(1) — just a few integers.
        """
        max_area = 0 
        n = len(heights)
        l = 0 
        r = n - 1 

        while l < r:
            # current container's width and bottleneck height
            width = r - l 
            height = min(heights[l], heights[r])
            area = width * height

            # update running max
            max_area = max(max_area, area)

            # move the shorter side inward — the only move that can improve area
            if heights[l] < heights[r]:
                l += 1 
            else:
                r -= 1 

        return max_area