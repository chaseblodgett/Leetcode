import string
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        banned = set(banned)
        paragraph = re.split(r'[,.!?\s]+',  paragraph)
        print(paragraph)

        for i in range(len(paragraph)):
            word = paragraph[i].translate(str.maketrans('', '', string.punctuation)).lower()
            paragraph[i] = word


        print(paragraph)
        max_word = ""
        max_num = 0
        for i in range(len(paragraph)):
            count = paragraph.count(paragraph[i])
            if paragraph[i] and paragraph[i] not in banned and count > max_num:
                max_word = paragraph[i]
                max_num = count
               

        return max_word