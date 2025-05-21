class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        lower = s.lower()

        for let in lower:
            if let.isalnum():
                stack.append(let)
        
        mid = len(stack) // 2
        for i in range(mid):
            if stack[i] != stack.pop():
                return False
        
        return True