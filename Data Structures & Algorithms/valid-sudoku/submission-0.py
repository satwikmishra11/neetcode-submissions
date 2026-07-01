class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] != '.':
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] != '.':
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        if board[row][col] != '.':
                            if board[row][col] in seen:
                                return False
                            seen.add(board[row][col])
        
        return True
        