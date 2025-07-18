class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        first = 0
        second = None

        for i in range(1, len(nums)):
            if nums[i] > nums[first]:
                second = first
                first = i
            elif second is None or nums[i] > nums[second]:
                second = i


        if (nums[first] / 2 ) >= nums[second]:
            return first
        
        return -1
      