class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])

        answer = []
        for i in range(m):
            answer.append([0] * n)
        for i in range(m):
            for j in range(n):
                
                startRow = 0 if i - k < 0 else i - k
                startCol = 0 if j - k < 0 else j - k
                endRow = m if i + k >= m else i + k + 1
                endCol = n if j + k >= n else j + k + 1
                for row in range(startRow, endRow):
                    answer[i][j] += sum(mat[row][startCol : endCol])
        
        return answer