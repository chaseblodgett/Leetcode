from collections import defaultdict, deque

class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        waiting = defaultdict(deque)

        for word in words:
            waiting[word[0]].append((word, 1)) 

        count = 0

        for c in s:
            
            old_bucket = waiting[c]
            waiting[c] = deque()  

            while old_bucket:
                word, idx = old_bucket.popleft()
                if idx == len(word):
                    count += 1 
                else:
                    next_char = word[idx]
                    waiting[next_char].append((word, idx + 1))

        return count
