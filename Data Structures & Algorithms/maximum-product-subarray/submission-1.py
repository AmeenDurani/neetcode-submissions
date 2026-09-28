class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        current_max = nums[0]
        current_min = nums[0]

        for num in nums[1:]:
            new_max = max(current_max * num, num, current_min * num)
            new_min = min(current_min * num, num, current_max * num)

            current_max = new_max
            current_min = new_min

            res = max(current_max, res)

        return res
