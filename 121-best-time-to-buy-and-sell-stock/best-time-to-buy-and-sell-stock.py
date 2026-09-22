class Solution(object):
    def maxProfit(self, prices):
        min=prices[0]
        max_profit=0
        min_index=0
        max_index=0
        for i in range(len(prices)):
            if prices[i]<min:
                min=prices[i]
            elif (prices[i]-min)>max_profit:
                max_profit=(prices[i]-min)
        return max_profit
            

            
            




