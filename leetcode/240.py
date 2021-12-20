"""
    240. Search a 2D Matrix II
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def is_in_row(row: List[int]) -> bool:
            return target in row
        
        return any(map(is_in_row, matrix))

"""
    - 164 ms 20.6 MB

    # Others
        1. two pointer - 148 ms 20.5 MB
            x, y = len(matrix[0]) - 1, 0

            while -1 < x and y < len(matrix):
                if matrix[y][x] > target:
                    x -= 1
                elif matrix[y][x] < target:
                    y += 1
                else:
                    return True
            
            return False
"""