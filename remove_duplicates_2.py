class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        k = 0
        i = 0
        while i < len(nums):
            count = 1
            j = i
            while j + 1 < len(nums) and nums[j] == nums[j+1]:
                count += 1
                j += 1
            
            if count > 1:
                nums[k] = nums[i]
                nums[k+1] = nums[i]
                k += 2
                i = j + 1
            else:
                nums[k] = nums[i]
                k += 1
                i += 1
        
        return k