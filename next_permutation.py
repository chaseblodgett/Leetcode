class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        

        i = len(nums) - 1

        while i - 1 >= 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        if i-1 == -1:
            nums.sort()
            return
        
        next_big = i
        for j in range(i-1, len(nums)):
            if nums[j] > nums[i-1] and nums[j] < nums[next_big]:
                next_big = j
        
        tmp = nums[i-1]
        nums[i-1] = nums[next_big]
        nums[next_big] = tmp

        nums[i:] = sorted(nums[i:])