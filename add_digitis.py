class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        string_num = str(num)

        while len(string_num) > 1:
            dig_sum = 0
            for i in range(len(string_num)):
                dig_sum += int(string_num[i])
            
            string_num = str(dig_sum)

        return int(string_num)