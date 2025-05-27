import math
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def rec(path, remaining, result):
            if not remaining:
                result.append(path)
                return
            
            for i in range(len(remaining)):
                new_path = list(path)
                new_path.append(remaining[i])

                front = remaining[:i]
                back = remaining[i+1:]
                front.extend(back)
         
                rec(new_path, front, result)

        result = []
        rec([], nums, result)

        return result