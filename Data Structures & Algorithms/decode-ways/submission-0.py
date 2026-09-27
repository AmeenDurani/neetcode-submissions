class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        prev = ""

        # base case, a single number.
        dp[0] = 1

        for i in range(1, n + 1):
            single = int(s[i - 1])
            double = int(prev + s[i - 1]) if prev != "0" else single

            # valid single.
            if 0 < single < 27:
                dp[i] += dp[i - 1]

            # valid double.
            if 27 > double > 9:
                dp[i] += dp[i - 2]
            
            prev = s[i - 1]

        return dp[n]