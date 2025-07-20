class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        my_dict = {}
        max_len = -1
        for i in range(len(s)):
            if s[i] not in my_dict.keys():
                my_dict[s[i]] = i
            elif i - my_dict[s[i]] - 1 > max_len:
                max_len = i - my_dict[s[i]] -1
        
        return max_len