prices = [10,1,1,6]

class Solution:
    def finalPrices(self, prices):
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if j > i and prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
        
        return prices

obj = Solution()
print(obj.finalPrices(prices))