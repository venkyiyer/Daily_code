prices = [7,1,5,3,6,4]

class Solution:
    def maxProfit(self, prices):
        l,r  = 0,0
        getmx = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                getmx= max(getmx, profit)
            else:
                l = r
            r+=1
        
        return getmx

obj = Solution()
print(obj.maxProfit(prices))