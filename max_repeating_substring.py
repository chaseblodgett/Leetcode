class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        
        k = 0
        
        while word in sequence:
            sequence = sequence.replace(word, "", 1)
            k += 1
        
        return k
