import math
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
    
        ret = []
        for i in range(rowIndex+1):

            ret.append(math.factorial(rowIndex) // (math.factorial(i) * math.factorial(rowIndex - i)))
        return ret
