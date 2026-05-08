class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque 
        rows, columns = len(grid), len(grid[0])

        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        islands = 0
        if not grid:
            return 0 
        
        seen = set()
        q = deque()
        def bfs(r, c):
            seen.add((r, c))
            q.append((r,c))

            while q:
                r, c = q.popleft()

                for dr, dc in DIRECTIONS:
                    nr, nc = r +dr, c +dc
                    if (0<=nr < rows and 
                    0 <= nc < columns and grid[nr][nc] == "1" and
                    ((nr, nc)) not in seen):
                        seen.add((nr, nc))
                        q.append((nr, nc))
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r, c) not in seen:
                    bfs(r, c)
                    islands +=1


        return islands



        