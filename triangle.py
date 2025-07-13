class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        mem = []

        for i in range(len(triangle)):
            mem.append([-1] * (i +1))
        
        def rec(i, j):
            if i >= len(triangle) or i < 0 or j >= len(triangle[i]) or j < 0:
                return 0
            
            if mem[i][j] != -1:
                return mem[i][j]
            
            mem[i][j] = triangle[i][j] + min(rec(i+1, j), rec(i+1, j+1))
            return mem[i][j]
        

        rec(0,0)
        return mem[0][0]