class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        count = 0

        for length in range(1, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length <= 2:
                        count += 1
                        dp[i][j] = True
                    else:
                        if dp[i + 1][j - 1]:
                            count += 1
                            dp[i][j] = True
        return count

