class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        curr_sum = 0
        max_sum = 0
        beg = 0
        end = 0
        curr_set = set()

        for i in range(len(nums)):
            if nums[i] not in curr_set:
                end = i
                curr_set.add(nums[i])
                curr_sum += nums[i]
                max_sum = max(curr_sum, max_sum)
            elif nums[i] in curr_set:
                while nums[beg] != nums[i]:
                    curr_sum -= nums[beg]
                    curr_set.remove(nums[beg])
                    beg += 1
                beg += 1
                max_sum = max(curr_sum, max_sum)
                end = i
            
        
        return max_sum