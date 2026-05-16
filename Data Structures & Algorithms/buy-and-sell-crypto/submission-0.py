class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0

        if len(prices) == 1:
            return profit
        for sell in range(1, len(prices)):
            current = prices[sell] - prices[buy]
            profit = max(profit, current)
            if prices[buy] > prices[sell]:
                buy = sell
            sell+=1
        return profit
