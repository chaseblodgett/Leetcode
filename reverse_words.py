class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        curr = ""
        ret = ""

        for i in range(len(s)):
            if s[i] != " ":
                curr += s[i]
            
            elif s[i] == " " and len(curr) > 0:
                ret = " " + curr + ret
                curr = ""

        return (curr + ret).strip()