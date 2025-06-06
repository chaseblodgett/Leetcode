class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])

        def dfs(i, j, idx):
            if idx == len(word):
                return True

            if i < 0 or j < 0 or i >= m or j >= n or word[idx] != board[i][j]:
                return False
            
            tmp = board[i][j]
            board[i][j] = "1"

            up = dfs(i+1, j, idx+1)
            down = dfs(i-1, j, idx+1)
            left = dfs(i, j+1, idx+1)
            right = dfs(i, j-1, idx+1)

            board[i][j] = tmp

            return up or left or down or right


        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
                
        return False