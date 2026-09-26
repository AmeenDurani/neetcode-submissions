class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, res = 0, 1, 0
        while r < len(prices):
            if prices[r] - prices[l] < 0:
                l = r
            else:
                res = max(prices[r] - prices[l], res)
                r += 1

        return res
        