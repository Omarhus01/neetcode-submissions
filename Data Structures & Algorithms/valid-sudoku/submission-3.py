class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict

        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)
        #matrix looping 
        for r in range(9):
            for c in range(9):
                honga = board[r][c]
                #ignoring conditions 
                if honga == ".":
                    continue
                #naming easability 
                box = (r//3, c//3)
                #checking condition
                if (honga in rows[r] or
                    honga in columns[c] or 
                    honga in boxes[box]):
                    return False
                #updating sets condition 
                rows[r].add(honga)
                columns[c].add(honga)
                boxes[box].add(honga)
        return True