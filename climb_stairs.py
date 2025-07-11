class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        mem = [-1] * (n+1)
        mem[0] = 1
        mem[1] = 2
        
        def rec(i):
            
            if mem[i] != -1:
                return mem[i] 
            
            mem[i] = rec(i-1) + rec(i-2)
            return mem[i]
        
        rec(n)
        return mem[n-1]