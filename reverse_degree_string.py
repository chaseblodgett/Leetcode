import string
from collections import defaultdict
class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = defaultdict(int)
        for i, letter in enumerate(string.ascii_lowercase):
            counts[letter] = 26 - i
        
        total = 0
        for i,let in enumerate(s):
            total += (i+1) * counts[let]
        
        return total