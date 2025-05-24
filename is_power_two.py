class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0: return False

        binary = bin(n)
        one_count = 0

        for num in binary:
            if num == "1":
                one_count += 1
        
        return one_count == 1