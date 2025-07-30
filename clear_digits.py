class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        

        ret = ""
        delete_count = 0

        for i in range(len(s)-1, -1, -1):
            if not s[i].isdigit() and delete_count == 0:
                ret = s[i] + ret
            elif not s[i].isdigit():
                delete_count -= 1
            elif s[i].isdigit():
                delete_count += 1
        
        return ret