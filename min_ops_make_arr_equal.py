class Solution:
    def minOperations(self, n: int) -> int:
        
        ret = 0

        for i in range(1, n, 2):
            ret += n - i
        
        return ret