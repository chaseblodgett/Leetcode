class Solution(object):

    def check_prime(self, n):
        if n == 2: return True
        for i in range(2, n):
            if n % i == 0: return False
        return True
    
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        if n == 1: return True

        while n > 0:
            if n % 2 ==0:
                n = n//2
            elif n % 3 ==0:
                n = n//3
            elif n % 5 ==0:
                n = n//5
            else:
                break
        return n == 1