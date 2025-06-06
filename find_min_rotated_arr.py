class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = 0
        r = len(nums) -1
        mid = (l + r) // 2

        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] > nums[l] and nums[mid] > nums[r]:
                l = mid + 1
            
            elif nums[mid] > nums[l] and nums[mid] < nums[r]:
                r = mid
            
            elif nums[mid] < nums[l] and nums[mid] < nums[r]:
                r = mid
            
            elif nums[mid] < nums[l] and nums[mid] > nums[r]:
                l = mid + 1

            else:
                break
            
        if mid < len(nums)-1 and nums[mid+1] < nums[mid]:
            return nums[mid+1]
        
        return nums[mid]