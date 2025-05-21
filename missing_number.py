class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numbers = set(nums)

        for i in range(len(nums)):
            if i not in numbers:
                return i

        return len(nums)    