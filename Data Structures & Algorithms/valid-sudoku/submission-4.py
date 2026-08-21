import math

class Solution:
    # [[1,2,3],[1,2,3]]
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku_nums = {'1','2','3','4','5','6','7','8','9'}

        if len(board) != 9:
            return False
        column_nums = defaultdict(set)
        box_nums = defaultdict(set) # math.floor n/3 for x,y

        for x, row in enumerate(board):
            if len(row) !=9:
                return False
            row_nums = set()
            for y, num in enumerate(row):
                if num == ".":
                    continue

                if num in row_nums or num not in sudoku_nums:
                    return False # No dupes, only valid nums
                row_nums.add(num)

                # Build column check across rows
                if num in column_nums[y] or num not in sudoku_nums:
                    return False
                column_nums[y].add(num)

                # Build box check across rows
                box_key = (math.floor(x/3), math.floor(y/3))
                if num in box_nums[box_key]:
                    return False
                box_nums[box_key].add(num)
        
        return True 
            


