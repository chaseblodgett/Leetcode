class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False

        my_dict = {}

        for i in range(len(s)):
            if s[i] not in my_dict.keys():
                my_dict[s[i]] = 1
            else:
                my_dict[s[i]] += 1

            if t[i] not in my_dict.keys():
               my_dict[t[i]] = -1
            else:
                my_dict[t[i]] -= 1
        
        for val in my_dict.values():
            if val != 0:
                return False
        
        return True