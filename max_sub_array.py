class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        curr_sum = 0
        curr_max = min(nums)

        for i in range(len(nums)):
            if curr_sum < 0:
                curr_sum = 0
            
            curr_sum += nums[i]
            
            if curr_sum >= curr_max:
                curr_max = curr_sum
        
        return curr_max