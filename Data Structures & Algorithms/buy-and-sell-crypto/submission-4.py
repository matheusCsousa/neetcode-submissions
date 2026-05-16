class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0

        for sell in range(1, len(prices)):
            current = prices[sell] - prices[buy]
            profit = max(profit, current)
            if prices[buy] > prices[sell]:
                buy = sell
        return profit
