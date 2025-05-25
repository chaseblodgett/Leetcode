# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        mid = (left + right) // 2
        direction = isBadVersion(mid)

        while left != mid and right != mid:
            if not direction: 
                left = mid
            else:
                right = mid
            
            mid = (left + right) // 2
            direction = isBadVersion(mid)

        if left == mid: return mid + 1
        return mid