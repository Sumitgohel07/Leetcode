class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for value in row:
                if value == '.':
                    continue 
                if value in seen:
                    return False
                seen.add(value)
        for i in range(len(board)):
            seen = set()
            for j in range(len(board)):
                if board[j][i]=='.':
                    continue
                if board[j][i] in seen:
                    return False
                seen.add(board[j][i])

        for box_row in range(0,9,3):
            for box_column in range(0,9,3):
                seen = set()
                for row in range(box_row,box_row+3):
                    for column in range(box_column,box_column+3):
                        if board[row][column] == '.':
                            continue
                        if board[row][column] in seen:
                            return False
                        seen.add(board[row][column])
        return True
