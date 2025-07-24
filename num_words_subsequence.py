
def findNumWords(s, words):

    count = 0
    for i in range(len(words)):
        k = 0

        for j in range(len(s)):
            if k < len(words[i]) and words[i][k] == s[j]:
                k += 1
        
        if k == len(words[i]):
            count += 1
    
    return count
