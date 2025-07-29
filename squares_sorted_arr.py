class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        

        left = 0
        right = 0
        ret = []
        size = len(nums)

        while right < size and nums[right] < 0:
            right += 1
    
        if right > 0:
            left = right - 1
        
        else:
            while right < size:
                ret.append(nums[right] * nums[right])
                right += 1

            return ret

        while right < size and left >= 0:
            if abs(nums[right]) < abs(nums[left]):
                ret.append(nums[right] * nums[right])
                right += 1
            else:
                ret.append(nums[left] * nums[left])
                left -= 1
        
        while left >= 0:
            ret.append(nums[left] * nums[left])
            left -= 1

        while right < size:
            ret.append(nums[right] * nums[right])
            right += 1

        return ret
