class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        
        minimum = 0
        maximum = 0
        mode = float(count.index(max(count)))

        for i in range(256):
            if count[i] != 0:
                minimum = float(i)
                break
        
        for i in range(255, -1, -1):
            if count[i] != 0:
                maximum = float(i)
                break
        
        num_elems = 0
        sum_elems = 0

        for i in range(256):
            num_elems += count[i]
            sum_elems += count[i] * i
        
        mean = float(sum_elems) / float(num_elems)
        median = 0

        is_odd = num_elems % 2 == 1
        mid1 = num_elems // 2
        mid2 = mid1 if is_odd else mid1 - 1

        cumulative = 0
        m1 = m2 = None

        for i in range(256):
            cumulative += count[i]

            if m1 is None and cumulative > mid2:
                m1 = i
            if m2 is None and cumulative > mid1:
                m2 = i
                break

        median = float((m1 + m2)) / 2 if not is_odd else m2
                
        return [minimum, maximum, mean, median, mode]

