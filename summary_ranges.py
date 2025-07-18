class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """


        ret = []

        if not nums:
            return ret
        
        i = 0

        while i < len(nums):
            a = str(nums[i])
            b = ""
            while i < len(nums) -1 and nums[i] + 1 == nums[i+1]:
                b = "->" + str(nums[i+1])
                i += 1
            
            ret.append(a+b)
            i += 1
        
        return ret