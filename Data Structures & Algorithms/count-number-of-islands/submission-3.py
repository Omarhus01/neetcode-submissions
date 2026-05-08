class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque 
        if not grid:
            return 0 
        rows, columns = len(grid), len(grid[0])

        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        islands = 0
        
        
        seen = set()
        q = deque()
        def bfs(r, c):
            # BUG #1: you had `seen.add(r, c)` and `q.append(r, c)`
            # set.add() and deque.append() take ONE argument, not two.
            # You need to wrap the coords as a tuple first: (r, c) is one object.
            seen.add((r, c))
            q.append((r,c))

            while q:
                r, c = q.popleft()
                # DIRECTIONS holds the 4 movement vectors as (dr, dc) tuples:
                # (1,0)=down, (-1,0)=up, (0,1)=right, (0,-1)=left.
                # Looping over it lets us check all 4 neighbors of (r, c) in one clean block
                # instead of writing 4 separate near-identical if-statements.
                for dr, dc in DIRECTIONS:
                    # Unpack the delta: dr = change in row, dc = change in column.
                    # Add it to the current cell to get the neighbor's coordinates.
                    # Example: at (2, 3) with (dr, dc) = (1, 0) -> (nr, nc) = (3, 3), the cell below.
                    nr, nc = r +dr, c +dc
                    if (0<=nr < rows and 
                    0 <= nc < columns and 
                    # BUG #2: you had `(nr, nc) == "1"`
                    # That compares the COORDINATE TUPLE to the string "1" -- always False.
                    # You wanted the VALUE at that position in the grid: grid[nr][nc].
                    grid[nr][nc] == "1" and
                    ((nr, nc)) not in seen):
                        # BUG #3: these two lines were unindented, sitting at the same
                        # level as the `if`. That meant they ran on EVERY iteration
                        # regardless of the bounds/value/seen checks. They belong
                        # INSIDE the `if` block.
                        seen.add((nr, nc))
                        q.append((nr, nc))
                        # BUG #4: you originally had `islands += 1` here, inside BFS.
                        # That counted every cell as its own island. The increment
                        # belongs in the outer loop -- one bump per island discovered,
                        # not per cell flooded. (Also: `islands` is in the enclosing
                        # scope, so mutating it from inside bfs would need `nonlocal`
                        # anyway. Moving it out sidesteps that entirely.)
        
        # BUG #5: this whole outer loop was missing in your first attempt.
        # bfs() was defined but never called. BFS only floods ONE island from a
        # given start -- you still need something that scans the grid to find
        # each new island's starting cell. That's what this loop does.
        for r in range(rows):
            for c in range(columns):
                # BUG #6: you originally had `grid[r][c] not in seen`.
                # `grid[r][c]` is the string "1" or "0", but `seen` holds tuples
                # like (r, c). You're checking the wrong thing against `seen`.
                # Use the coordinate: `(r, c) not in seen`.
                if grid[r][c] == "1" and (r, c) not in seen:
                    bfs(r, c)
                    # Increment lives HERE -- once per island actually discovered.
                    islands +=1


        return islands