class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row_set = set()
        col_set = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    col_set.add(j)
                    row_set.add(i)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in row_set or j in col_set:
                    matrix[i][j] = 0