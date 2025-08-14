class Solution(object):
    def minFlips(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m = len(grid)
        n = len(grid[0])
        
        row_flips = 0
        col_flips = 0

        for i in range(m):
            for j in range(n//2):

                if grid[i][j] != grid[i][n-1-j]:
                    row_flips += 1
        

        for i in range(n):
            for j in range(m//2):
                if grid[j][i] != grid[m-j-1][i]:
                    col_flips += 1


        return min(row_flips, col_flips)