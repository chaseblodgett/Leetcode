class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        arr = s.split(" ")

        if len(arr) != len(pattern):
            return False
        
        dict_pat = {}
        dict_str = {}
        for i in range(len(pattern)):
            if pattern[i] in dict_pat.keys() and dict_pat[pattern[i]] != arr[i]:
                return False
            
            elif arr[i] in dict_str.keys() and dict_str[arr[i]] != pattern[i]:
                return False
        
            dict_pat[pattern[i]] = arr[i]
            dict_str[arr[i]] = pattern[i]

        return True