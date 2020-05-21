class Solution:
    def countSquares(self, matrix):
        if len(matrix) == 0 or matrix is None:
            return 0
        
        result = 0
        
        row = len(matrix)
        col = len(matrix[0])
        
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 1:
                    if r == 0 or c == 0:
                        result += 1
                    else:
                        value = min(matrix[r-1][c-1], matrix[r][c-1], matrix[r-1][c]) + matrix[r][c]
                        result += value
                        matrix[r][c] = value
        return result