class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def rec(i, curr, nums, ret):
            
            if len(curr) == k:
                ret.append(list(curr))
                return
            
            if i >= len(nums):
                return

            curr.append(nums[i])
            rec(i+1, curr, nums, ret)

            curr.pop()
            rec(i+1, curr, nums, ret)

        nums = []
        ret = []
        for i in range(1,n+1):
            nums.append(i)

        rec(0, [], nums, ret)

    
        return ret