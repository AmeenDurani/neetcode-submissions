class Solution:
    def search(self, n: List[int], t: int) -> int:
        l, r = 0, len(n) - 1
        m =  (l + r) // 2

        while l != r:
            if n[m] == t:
                return m

            if n[l] <= n[m] and n[l] <= t <= n[m]:
                # left half sorted, and in range.
                r = m - 1
            elif n[l] <= n[m]:
                # left half sorted, not in range.
                l = m + 1
            elif n[m] <= n[r] and n[m] <= t <= n[r]:
                # right half sorted, and in range.
                l = m + 1
            else:
                # right half sorted, not in range.
                r = m - 1
            
            m =  (l + r) // 2
        
        if t != n[m]: return - 1
        return m
