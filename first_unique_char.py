from collections import defaultdict
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        my_dict = defaultdict(int)
        for let in s:
            my_dict[let] += 1
        
        for i in range(len(s)):
            if my_dict[s[i]] <= 1:
                return i
        
        return -1