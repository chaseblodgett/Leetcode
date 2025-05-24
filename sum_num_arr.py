class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if len(nums) == 0:
            self.arr = []
        else:
            self.arr = [nums[0]]

        for i in range(1,len(nums)):
            self.arr.append(nums[i] + self.arr[i-1])
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.arr[right]
        else:
            return self.arr[right] - self.arr[left-1]