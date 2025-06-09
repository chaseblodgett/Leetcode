class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(nums) -1
        mid = (left + right) // 2

        while left < right:
            mid = (left + right) // 2

            if nums[left] > nums[left+1]:
                return left
            
            elif nums[right] > nums[right-1]:
                return right
            
            elif nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            
            elif nums[mid] < nums[mid-1]:
                right = mid-1
            
            elif nums[mid] < nums[mid+1]:
                left = mid + 1
        
        return mid