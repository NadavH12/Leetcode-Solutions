class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        """Naive Solution O(N^2)"""
        """
        max_profit = -1 * float("inf")

        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1,len(prices)):
                sell = prices[j]
                profit = sell - buy
                if profit > max_profit:
                    max_profit = profit

        if max_profit < 0:
            return 0

        return max_profit
        """



        """Sliding Window"""
        max_profit = -1 * float("inf")
        
        left = 0
        right = 1

        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit > max_profit:
                max_profit = profit

            if prices[left] > prices[right]:
                left = right
                right += 1
                continue

            else:
                right += 1
                continue

        if max_profit < 0:
            return 0

        return max_profit


