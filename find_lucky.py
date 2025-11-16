from collections import defaultdict

class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        _dict = defaultdict(int)

        for num in arr:
            _dict[num] += 1
        
        ret = -1

        for key,val in _dict.items():
            if key == val and val > ret:
                ret = val

        return ret