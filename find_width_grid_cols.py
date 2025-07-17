class Solution(object):
    def findColumnWidth(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        
        m = len(grid)
        n = len(grid[0])
        ans = []


        for i in range(n):
            max_length = 0
            for j in range(m):

                max_length = max(max_length, len(str(grid[j][i])) )
            
            ans.append(max_length)
        
        return ans