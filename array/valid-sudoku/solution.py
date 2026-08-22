from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(0,9):
            for col in range(0,9):
                value = board[row][col]

                box = (row // 3) * 3 + (col // 3)

                if value == ".":
                    continue

                if value in rows[row]:
                    return False
                
                if value in columns[col]:
                    return False
                
                if value in boxes[box] :
                    return False

                rows[row].add(value)
                columns[col].add(value)
                boxes[box].add(value)

        
        return True
