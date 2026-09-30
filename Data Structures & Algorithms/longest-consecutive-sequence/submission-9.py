class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        for num in nums:
            if num - 1 in nums:
                continue
            
            length = 0
            while num + length in nums:
                length += 1
            
            res = max(res, length)
        return res
        