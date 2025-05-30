class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        path_counts = [([-1] * n) for _ in range(m)]

        def rec(i, j):

            if i == m-1 and j == n-1:
                return 1
            
            if i >= m or j >= n:
                return 0
            
            if path_counts[i][j] != -1:
                return path_counts[i][j]

            path_counts[i][j] = rec(i+1, j) + rec(i, j+1)

            return path_counts[i][j]

        return rec(0, 0)