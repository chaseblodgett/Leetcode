class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            rev_x = "-" + str(x)[::-1][:-1]
            i = 1
        elif x > 0:
            rev_x = str(x)[::-1]
            i = 0
        else:
            return 0

        print(rev_x)
        while(rev_x[i] == "0"):
            i += 1

        if x < 0:
            rev_x = "-" + (rev_x[i:])
            ret = int(rev_x)
        else:
            ret = int(rev_x[i:])

        if(ret < -2**31 or ret > 2**31 -1):
            return 0
        return ret