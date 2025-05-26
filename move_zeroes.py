class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        non_zero_count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                non_zero_count += 1
        
        for i in range(non_zero_count):
            if nums[i] == 0:
                next_non_zero = i + 1
                while next_non_zero < len(nums) and nums[next_non_zero] == 0:
                    next_non_zero += 1
                
                nums[i] = nums[next_non_zero]
                nums[next_non_zero] = 0