prices = [7,6,4,3,1]

l , r = 0,1 
maxProfit = 0

while r < len(prices):
    if prices[l] < prices[r]:
        profit = prices[r] - prices[l]
        maxProfit += profit 
        l+=1   
    else:
        l=r
    r+=1

print(maxProfit)