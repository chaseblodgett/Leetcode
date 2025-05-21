class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        elif len(nums) == 1 and nums[0] == target:
            return [0, 0]
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        while nums[mid] != target and right > left:
            if nums[mid] < target:
                left = mid + 1
                mid = (left + right) // 2
                
            elif nums[mid] > target:
                right = mid
                mid = (left + right) // 2

        if left > right:
            return [-1, -1]
        
        if left == right and nums[left] != target:
            return [-1, -1]

        left = mid
        right = mid
        while left > 0 and nums[left-1] == target:
            left -= 1
        
        while right < len(nums)-1 and nums[right+1] == target:
            right += 1
        
        return [left, right]