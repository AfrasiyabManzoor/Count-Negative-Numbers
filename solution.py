class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        negatives = 0

        j = n-1
        for i in range(m):
            count = 0
            while j >= 0 and grid[i][j] < 0:
                j -= 1
                count += 1
            negatives += count * (m-i) 

        return negatives
