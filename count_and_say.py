class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        def rec(i, n, rle):
            if i == n:
                return rle
            
            count = 0
            prev_let = rle[0]
            new_rle = ""
            for let in rle:
                if let != prev_let:
                    new_rle += str(count) + str(prev_let)
                    prev_let = let
                    count = 1
                else:
                    count += 1
            
            new_rle += str(count) + str(prev_let)
            return rec(i+1, n, new_rle)

        
        return rec(1, n, "1")