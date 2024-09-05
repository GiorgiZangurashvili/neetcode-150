# You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:
# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

# Note: A board does not need to be full or be solvable to be valid.

# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

class Solution:
    def isValidRow(self, board: List[List[str]], row: int) -> bool:
        hashset = set()

        for col in range(9):
            value = board[row][col]
            if value.isdigit():
                if value in hashset:
                    return False
                else:
                    hashset.add(value)
        return True

    def isValidCol(self, board: List[List[str]], col: int) -> bool:
        hashset = set()

        for row in range(9):
            value = board[row][col]
            if value.isdigit():
                if value in hashset:
                    return False
                else:
                    hashset.add(value)
        return True
    
    def isValidSubBox(self, board: List[List[str]], startRow: int, startCol: int) -> bool:
        hashset = set()

        for rowInc in range(3):
            for colInc in range(3):
                value = board[startRow + rowInc][startCol + colInc]
                if value.isdigit():
                    if value in hashset:
                        return False
                    else:
                        hashset.add(value)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            if not self.isValidRow(board, row):
                return False
        
        for col in range(9):
            if not self.isValidCol(board, col):
                return False
        
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                if not self.isValidSubBox(board, row, col):
                    return False
        
        return True
