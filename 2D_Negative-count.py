class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg = 0
        for row in grid:
            for col in row:
                if col < 0:
                    neg += 1
        return(neg)
