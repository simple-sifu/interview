# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
# You may choose a single day to buy one NeetCoin and choose a different day in the future 
# to sell it. Return the maximum profit you can achieve. You may choose to not make any 
# transactions, in which case the profit would be 0.


class Solution:

    def bestTimeToBuy(self, prices: list[int]):
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1

        return maxProfit


sol = Solution()
prices = [10,1,5,6,7,1]
print (sol.bestTimeToBuy(prices))
# Output: 6

prices =  [5,1,5,6,7,1,10]
print (sol.bestTimeToBuy(prices))
# Output: 9
