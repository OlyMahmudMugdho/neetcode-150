class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profits = [0]

        buy = 0
        sell = 0
        profit = 0

        i = 0
        while(i < len(prices)):
            if i == 0:
                buy = prices[0]
                i += 1
                continue

            if prices[i] < buy:
                buy = prices[i]
                sell = 0
                i += 1
                continue

            sell = max(sell, prices[i])

            profit = sell - buy

            profits.append(profit)

            i += 1

        return max(profits)
        