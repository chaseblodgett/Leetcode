
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        my_dict = {}
        t_dict = {}
        for i in range(len(s)):
            
            if s[i] in my_dict.keys() and t[i] != my_dict[s[i]]:
                return False
            elif t[i] in t_dict.keys() and s[i] != t_dict[t[i]]:
                return False
            elif s[i] not in my_dict.keys():
                my_dict[s[i]] = t[i]
                t_dict[t[i]] = s[i]
        
        return True