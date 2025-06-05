class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        n = len(grid)
        m = len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] != '1':
                return
            grid[i][j] = '0' 
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count