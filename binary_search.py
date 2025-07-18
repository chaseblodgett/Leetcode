class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        low = 0
        high = len(nums)

        while low < high:
            mid = (low + high) // 2

            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid
            else:
                return mid
        
        return -1 