class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        sentence_list = sentence.split()

        for i in range(len(sentence_list)):
            replacement = ""
            for root in dictionary:
                if sentence_list[i].startswith(root) and replacement == "":
                    sentence_list[i] = root
                    replacement = root
                elif sentence_list[i].startswith(root) and len(root) < len(replacement):
                    sentence_list[i] = root
                    replacement = root
        
        return ' '.join(sentence_list)