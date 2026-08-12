class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        res = 0
        while right < len(prices):
            res = max(prices[right] - prices[left], res)
            if prices[left] > prices[right]:
                left = right
            right += 1
        
        return res


