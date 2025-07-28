class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        large = -1
        small = -1

        for let in s:
            if let.isdigit() and int(let) > small and int(let) < large:
                small = int(let)
            elif let.isdigit() and int(let) > large:
                small = large
                large = int(let)

        return small