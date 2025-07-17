class Solution(object):
    def checkXMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == j or i + j == len(grid) -1:
                    if grid[i][j] == 0:
                        return False
                elif grid[i][j] != 0:
                    return False

        return True