class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        the plan here is ti use hashsets ast his will gurantee the removal of duplicates
        we can do that by checking the numbers board[r][c] and then see if it exists in any of the 
        rows, columns or boxes, and ffom rthere we can immediately return false
        the key point was the boxes and how we get them and I learned that by looking at th eintger 
        division 
        as it was helpful adn making weach box unique going form (0, 0 )  -> (2,2) boxes in the board 
        if things are fine, we add the value we found in all o f the rows, columns and boxes
        and we don't forget to ignore the emoty entries 

        """
        from collections import defaultdict

        rows = defaultdict(set) #keys are the rows' numbers 
        columns = defaultdict(set) # keys are th ecolumns' number 
        boxes = defaultdict(set) # keys ar ea tuple of the integer divion of the r and c

        for r in range(9):
            for c in range(9):
                if board[r][c]== ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in columns[c] or
                    board[r][c] in boxes[(r//3, c//3)]):
                    return False
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                boxes[(r//3, c//3)].add(board[r][c])
        return True   