class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        ret = ""
        for i in range(len(word)):
            ret = word[i] + ret
            if word[i] == ch:
                return ret + word[i+1:]
        
        return word