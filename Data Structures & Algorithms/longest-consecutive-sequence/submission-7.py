class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        for n in s:
            if n - 1 in s:
                continue

            local_counter = 1
            while n + 1 in s:
                local_counter += 1
                n += 1
            
            res = max(res, local_counter)
        
        return res
        