class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force
        maxP = 0
        for i in range(len(prices)):
            for j in range (i+1,len(prices)):
                diff = prices[j]-prices[i]
                if diff > maxP:
                    maxP = diff
        
        return maxP
        