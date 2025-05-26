from collections import defaultdict
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        nums1_dict = defaultdict(int)
        nums2_dict = defaultdict(int)

        for num in nums1:
            nums1_dict[str(num)] += 1
        
        for num in nums2:
            if str(num) in nums1_dict.keys():
                nums2_dict[str(num)] += 1
        
        ret = []
        for key in nums1_dict.keys():
            for i in range(min(nums1_dict[key], nums2_dict[key])):
                ret.append(int(key))
        
        return ret