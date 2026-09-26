class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums), 1):
            res[i] = res[i - 1] * nums[i - 1]
        
        cur_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= cur_prod
            cur_prod *= nums[i]
        
        return res