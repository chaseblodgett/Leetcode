class Solution(object):
    def checkValidGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        
        if grid[0][0] != 0:
            return False
        
        directions = [ 
            (1 ,2),
            (2, 1),
            (-1, 2),
            (-2, 1),
            (-1, -2),
            (-2, -1),
            (1, -2),
            (2, -1)
        ]

        n = len(grid)
        for i in range(n):
            for j in range(n):

                is_valid = False
                if (i,j) == (0, 0):
                    continue
            
                for dx, dy in directions:
                    row = i + dx
                    col = j + dy
                    if row >= 0 and row < n and col >=0 and col < n:
                        if grid[row][col] == grid[i][j] -  1:
                            is_valid = True
                            
                if not is_valid:
                    return False
        
        return True