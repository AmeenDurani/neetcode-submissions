class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        s = set(nums)

        for num in s:
            if num - 1 in s:
                continue
            
            l = 1
            while num + l in s:
                l += 1
            
            res = max(res, l)

        return res        