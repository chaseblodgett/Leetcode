class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        max_sum = float('-inf')

        for i in range(n - 2):
            for j in range(m - 2):
                curr_sum = (
                    grid[i][j] + grid[i][j+1] + grid[i][j+2] +
                                grid[i+1][j+1] +
                    grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                )
                max_sum = max(max_sum, curr_sum)

        return max_sum