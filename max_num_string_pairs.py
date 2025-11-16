class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        word_set = set()
        count = 0
        for i in range(len(words)-1, -1, -1):
            if (words[i][1] + words[i][0]) in word_set:
                count += 1
            word_set.add(words[i])
        
        return count