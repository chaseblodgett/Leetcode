import math
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        n = math.pow(2, len(nums))
        def rec(curr, subsets, idx, n):
            if n == 0:
                return

            subsets.append(curr)

            for i in range(idx, len(nums)):
                if nums[i] not in curr:
                    new_curr = list(curr)
                    new_curr.append(nums[i])
                    rec(new_curr, subsets, i+1, n-1)

        
        curr = []
        subsets = []
        rec(curr, subsets,0,  n)

        return subsets