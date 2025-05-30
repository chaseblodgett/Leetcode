import math

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m = len(grid)
        n = len(grid[m-1])

        memo = [([-1] * n) for _ in range(m)]

        def rec(i, j):

            if i >= m or j >= n:
                return float('inf')
            
            if i == m - 1 and j == n -1:
                memo[i][j] = grid[i][j]
                return grid[i][j]
            
            if memo[i][j] != -1:
                return memo[i][j] 
            
            memo[i][j] = grid[i][j] + min(rec(i+1, j), rec(i, j+1))

            return memo[i][j]
        
        rec(0, 0)
        print(memo)
        return memo[0][0]