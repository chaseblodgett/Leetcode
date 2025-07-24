class Solution(object):
    def minNumber(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        num1 = min(nums1)
        num2 = min(nums2)

        num2_set = set(nums2)
        nums3 = []
        for num in nums1:
            if num in num2_set:
                nums3.append(num)

        if nums3:
            return min(nums3)

        if num1 == num2:
            return num1
        
        if num1 < num2:
            return int(str(num1) + str(num2))
        
        return int(str(num2) + str(num1))