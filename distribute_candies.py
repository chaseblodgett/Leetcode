class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        
        n = len(candyType)
        my_set = set()
        count = 0

        for candy in candyType:
            if candy not in my_set:
                my_set.add(candy)
                count += 1
        

        return min(n/2, count)