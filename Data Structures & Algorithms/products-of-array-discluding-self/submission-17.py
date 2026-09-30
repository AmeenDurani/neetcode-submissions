class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        for i in range(n):
            if not i:
                continue
            res[i] *= res[i - 1] * nums[i - 1]

        right_prod = 1
        for i in range(n - 1, -1, -1):
            if i != n - 1:
                res[i] *= right_prod

            right_prod *= nums[i]
        return res
        