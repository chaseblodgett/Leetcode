class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        h = 0
        v = 0

        hill = False
        valley = False

        for i in range(len(nums)-1):
            if hill and nums[i+1] < nums[i]:
                h += 1
            elif valley and nums[i+1] > nums[i]:
                v += 1

            if nums[i+1] < nums[i]:
                valley = True
                hill = False
            elif nums[i+1] > nums[i]:
                valley = False
                hill = True
        
        return h + v
        