class Solution(object):

    def merge_arr(self, arr, left, mid, right):
        left_len = mid - left + 1
        right_len = right - mid

        l = [0] * left_len
        r = [0] * right_len

        for i in range(left_len):
            l[i] = arr[left + i]
        for i in range(right_len):
            r[i] = arr[mid + i + 1]
        
        i = 0
        j = 0
        k = left
        while i < left_len and j < right_len:
            if l[i][0] <= r[j][0]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1
        
        while i < left_len:
            arr[k] = l[i]
            i+=1
            k+=1
        
        while j < right_len:
            arr[k] = r[j]
            j+=1
            k+=1
            
    def merge_sort(self, left, right, arr):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(left, mid, arr)
            self.merge_sort(mid+1, right, arr)
            self.merge_arr(arr, left, mid, right)

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        self.merge_sort(0, len(intervals) -1, intervals)
        
        ret = []
        curr = intervals[0]
        for i in range(len(intervals)):
            if curr[1] >= intervals[i][0] and intervals[i][1] > curr[1]:
                curr[1] = intervals[i][1]
            elif curr[1] < intervals[i][0]:
                ret.append(curr)
                curr = intervals[i]
        
        ret.append(curr)
        return ret