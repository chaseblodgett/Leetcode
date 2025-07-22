class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])

        mins = []
        for i in range(m):
            mins.append(min(matrix[i]))

        maxs = []
        for i in range(n):
            max_num = -1
            for j in range(m):
                if matrix[j][i] > max_num:
                    max_num = matrix[j][i]
            maxs.append(max_num)

        maxs = set(maxs)

        ret = []
        for num in mins:
            if num in maxs:
                ret.append(num)

        return ret