from collections import defaultdict
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """


        nums1_set = set(nums1)
        nums2_set = set(nums2)
        
        ret = []
        for i in range(1001):
            if i in nums1_set and i in nums2_set:
                ret.append(i)
                nums1_set.remove(i)
                nums2_set.remove(i)

        return ret