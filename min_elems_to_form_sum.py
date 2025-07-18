class Solution(object):
    def minElements(self, nums, limit, goal):
        """
        :type nums: List[int]
        :type limit: int
        :type goal: int
        :rtype: int
        """
        
        curr_sum = sum(nums)

        if curr_sum == goal:
            return 0
        
        difference = abs(goal - curr_sum)
        count = difference // limit
        extra = difference % limit

        if extra != 0:
            return count + 1
        return count