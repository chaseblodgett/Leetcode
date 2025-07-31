from collections import defaultdict
class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """

        curr_longest = ""

        for word in dictionary:
            
            idx = 0

            for i in range(len(s)):
                
                if idx < len(word) and word[idx] == s[i]:
                    idx += 1

            if idx == len(word) and len(word) > len(curr_longest):
                curr_longest = word
            elif idx == len(word) and len(word) == len(curr_longest) and word < curr_longest:
                curr_longest = word
            
        return curr_longest