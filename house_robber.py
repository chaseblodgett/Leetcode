class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        money = [0] * len(nums)
        k = 0

        while k < len(nums):
            if k == 0:
                money[k] = nums[k]
            elif k == 1:
                money[k] = max(nums[k], nums[k-1])
            else:
                money[k] = max(nums[k] + money[k-2], money[k-1])
            k+=1
        
        if k <= 2:
            return max(nums)
        return money[k-1]