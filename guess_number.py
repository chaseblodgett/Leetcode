# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        mid = n // 2
        my_guess = guess(mid)

        while my_guess != 0:
            if my_guess < 0:
                right = mid
            elif my_guess > 0:
                left = mid + 1
            mid = (left + right) // 2
            my_guess = guess(mid)

        return mid