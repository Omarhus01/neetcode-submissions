class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        PLAN

        Brute force: for each day i, walk forward until we find a warmer day.
        That's O(n²) — for each i, we might scan everything to its right.

        Key insight: a "monotonic decreasing stack" of INDICES. The stack
        holds indices of days still waiting for a warmer day. We never push
        an index until any earlier days it can resolve have been resolved.

        Why indices, not temperatures: when we resolve a waiting day j, we
        need to know the GAP (i - j), not just the temperatures. Indices
        give us both — temperatures[j] is one lookup away.

        Walk i from 0 to n-1. For each i:
          - While stack non-empty AND temperatures[i] > temperatures[stack[-1]]:
            * The top index j has been waiting; today is its warmer day.
            * Pop j and set res[j] = i - j.
            * Keep popping — i might resolve multiple waiting days in a row
              (if today is warmer than several earlier days that were each
              colder than the one before them).
          - Push i onto the stack — now i itself waits for a future warmer day.

        After the loop, anything left in the stack never found a warmer day.
        Their res entries stay at 0 (the initialized value), which is the
        correct answer per the problem.

        Why O(n) despite the nested loop: each index is pushed exactly once
        and popped at most once. Total work across all inner whiles is bounded
        by n. Outer loop is n iterations. Total O(n).

        Time:  O(n)
        Space: O(n) — the stack can hold up to n indices in the worst case
                       (e.g., strictly decreasing temperatures).
        """
        n = len(temperatures)
        res = [0] * n          # default 0 — correct for days that never see a warmer one
        stack = []             # holds INDICES of days still waiting for warmer

        for i in range(n):
            # while today (i) is warmer than the day at the top of the stack,
            # we've found that waiting day's answer
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()         # j was waiting; today resolves it
                res[j] = i - j          # gap in days = the answer for day j
            
            # i now joins the stack as a waiting day
            stack.append(i)

        return res