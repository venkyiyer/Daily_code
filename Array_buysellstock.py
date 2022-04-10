class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0   

        max_profit = sell_price = 0
        for price in prices[::-1]:
            sell_price = max(sell_price, price)
            max_profit = max(max_profit, sell_price - price)
        return max_profit

obj = Solution()
print(obj.maxProfit([7,1,5,3,6,4]))