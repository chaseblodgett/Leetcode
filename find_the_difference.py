from collections import defaultdict
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        my_dict = defaultdict(int)
        for let in s:
            my_dict[let] += 1
        
        for let in t:
            my_dict[let] -= 1
            if my_dict[let] < 0:
                return let