class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        curr_max = 0
        curr_profit = 0

        for i in range(len(prices) - 1, -1, -1):
            if prices[i] > curr_max:
                curr_max = prices[i]
            if curr_max - prices[i] > curr_profit:
                curr_profit = curr_max - prices[i]
        
        return curr_profit