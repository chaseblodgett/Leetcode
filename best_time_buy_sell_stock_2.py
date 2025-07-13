class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        high = prices[len(prices)-1]
        profit = 0

        for i in range(len(prices)-1, -1, -1):
            if prices[i] < high:
                profit += high - prices[i]
                high = prices[i]
            else:
                high = prices[i]

        return profit