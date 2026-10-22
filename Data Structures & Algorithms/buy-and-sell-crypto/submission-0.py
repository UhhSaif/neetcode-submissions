class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profitMax = 0
        cur = prices[0]
        for i in range(len(prices)):
            if prices[i] < cur:
                cur = prices[i]
            
            profit = prices[i] - cur
            if profit > profitMax:
                profitMax = profit

        return profitMax