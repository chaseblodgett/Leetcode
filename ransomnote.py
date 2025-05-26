from collections import defaultdict
class Solution(object):
    
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        r_dict = defaultdict(int)
        m_dict = defaultdict(int)

        for let in magazine:
            m_dict[let] += 1
        
        for let in ransomNote:
            r_dict[let] += 1
        
        for let in ransomNote:
            if let not in m_dict.keys(): 
                return False
            elif m_dict[let] < r_dict[let]:
                return False
        
        return True