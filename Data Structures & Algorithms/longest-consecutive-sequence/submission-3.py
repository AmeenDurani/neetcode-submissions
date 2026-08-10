class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(1) lookup
        hs = set(nums)
        res = 0
        for num in hs:
            if (num - 1) not in hs:
                # start of a sequence, start counting forwards
                cur_max = 1
                while (num + 1) in hs:
                    cur_max += 1
                    num += 1
                res = max(res, cur_max)
        return res