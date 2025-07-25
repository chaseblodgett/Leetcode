class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return 2

        return 1