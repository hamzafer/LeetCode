class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxProfit=0

        for i in range(0, len(prices)-1):
            if(prices[r]-prices[l] > 0):
                maxProfit = max(maxProfit, prices[r]-prices[l])
            else:
                l=r
            r+=1
        return maxProfit