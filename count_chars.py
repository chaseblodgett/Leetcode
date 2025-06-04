class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        my_dict = {}
        
        for char in chars:
            if char in my_dict.keys():
                my_dict[char] += 1
            else:
                my_dict[char] = 1
        
        ret = 0
        for word in words:
            new_dict = my_dict.copy()
            can_form_word = True
            
            for let in word:
                if let not in new_dict.keys() or new_dict[let] == 0:
                    can_form_word = False
                    break
                new_dict[let] -= 1
            
            if can_form_word:
                ret += len(word)
        
        return ret