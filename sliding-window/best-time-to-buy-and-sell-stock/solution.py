class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        i = 1

        while(i < len(prices)):
            price = prices[i]
            min_price = min(price, min_price)
            profit = price - min_price
            max_profit = max(profit, max_profit)

            i += 1

        return max_profit