class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict

        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                honga = board[r][c]
                if honga == ".":
                    continue
                box = (r//3, c//3)
                if (honga in rows[r] or
                    honga in columns[c] or 
                    honga in boxes[box]):
                    return False
                
                rows[r].add(honga)
                columns[c].add(honga)
                boxes[box].add(honga)
        return True