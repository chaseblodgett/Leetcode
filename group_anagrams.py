class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)
        
        for word in strs:
            s = ''.join(sorted(word))
            d[s].append(word)
        
        return d.values()
        

        