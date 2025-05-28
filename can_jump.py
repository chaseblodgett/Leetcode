class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) == 1:
            return True
        curr_end = len(nums) -1
    
        for i in range(curr_end -1, -1, -1):
            if i == 0 and nums[i] >= curr_end:
                return True
            if nums[i] >= curr_end - i:
                curr_end = i
    

        return False