class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = (rows * cols)
        
        if left == right and matrix[0][0] == target:
            return True

        while left < right:

            mid = (left + right) // 2

            row = mid // cols
            col = mid % cols

            if matrix[row][col] < target:
                left = mid + 1
            
            elif matrix[row][col] > target:
                right = mid
            
            else:
                return True
        
        return False