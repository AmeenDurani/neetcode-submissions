class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(nums: List[int]) -> int:
            # init
            n = len(nums)
            dp = [0] * n
            dp[0] = nums[0]

            # base case
            if n > 1:
                dp[1] = max(nums[0], nums[1])
            
            # tabulate
            for i in range(2, n):
                dp[i] = max(
                    dp[i - 2] + nums[i],
                    dp[i - 1]
                )
            
            return dp[-1]

        n = len(nums)
        c1 = rob_linear(nums[0 : n - 1]) if n > 1 else nums[0]
        c2 = rob_linear(nums[1: n]) if n > 1 else 0

        return max(c1, c2)          
            