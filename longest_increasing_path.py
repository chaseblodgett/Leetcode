class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        n, m = len(matrix), len(matrix[0])
        memo = [[-1] * m for _ in range(n)]

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

        def dfs(i, j):
            if memo[i][j] != -1:
                return memo[i][j]

            max_length = 1 
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] > matrix[i][j]:
                    length = 1 + dfs(ni, nj)
                    max_length = max(max_length, length)

            memo[i][j] = max_length
            return max_length