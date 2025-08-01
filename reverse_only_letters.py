

class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        left = 0
        right = len(s) -1
        s = list(s)

        while left < right:

            if s[left].isalpha() and s[right].isalpha():
                tmp = s[left]
                s[left] = s[right]
                s[right] = tmp
                left += 1
                right -= 1
            
            elif not s[left].isalpha() and s[right].isalpha():
                left += 1
            
            elif s[left].isalpha() and not s[right].isalpha():
                right -= 1
            
            elif not s[left].isalpha() and not s[right].isalpha():
                left += 1
                right -= 1
        
        return "".join(s)