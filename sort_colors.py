class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        my_dict = {}
        my_dict[0] = 0
        my_dict[1] = 0
        my_dict[2] = 0

        for i in nums:
            my_dict[i] += 1
        
        for i in range(my_dict[0]):
            nums[i] = 0

        for i in range(my_dict[1]):
            nums[i + my_dict[0]] = 1
        
        for i in range(my_dict[2]):
            nums[i + my_dict[1] + my_dict[0]] = 2