class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if (len(prices) < 2):
            return 0



        left = 0
        right = 1
        profit = 0

        while (right < len(prices)):
            if (prices[right] - prices[left] > 0):
                profit += (prices[right] - prices[left])
            left += 1
            right += 1


        return profit 
