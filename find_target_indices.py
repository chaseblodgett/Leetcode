class Solution(object):

    def merge(self, arr, left, mid, right):
        left_len = mid - left + 1
        right_len = right - mid

        l = [0] * left_len
        r = [0] * right_len
        
        for i in range(left_len):
            l[i] = arr[i + left]
        
        for j in range(right_len):
            r[j] = arr[j + mid + 1]
        
        i = 0
        j = 0
        k = left

        while i < left_len and j < right_len:
            if l[i] <= r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1
        
        while i < left_len:
            arr[k] = l[i]
            i += 1
            k += 1
        
        while j < right_len:
            arr[k] = r[j]
            j += 1
            k += 1
        
    def merge_sort(self, arr, left, right):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(arr, left, mid)
            self.merge_sort(arr, mid + 1, right)
            self.merge(arr, left, mid, right)

        return arr

    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = self.merge_sort(nums, 0, len(nums)-1)
        ret = []
        for i, elem in enumerate(nums):
            if elem == target:
                ret.append(i)

        return ret