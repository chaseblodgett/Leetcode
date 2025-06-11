class Solution(object):
    def sumOfNumberAndReverse(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return True
            
        for i in range(num):
            ret = ""
            for let in str(i):
                ret = let + ret
            
            if int(ret) + i == num:
                return True
        
        return False

                
            