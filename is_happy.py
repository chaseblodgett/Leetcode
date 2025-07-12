import math
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        my_set = set()

        while True:
            num_str = str(n)
            n = 0
            for num in num_str:
                n += int(math.pow(int(num), 2))
            
            if n == 1:
                return True
            
            if n in my_set:
                return False
            
            my_set.add(n)