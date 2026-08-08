class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1] * l
        for i in range(l):
            if i == 0:
                continue
            
            prev = i-1
            res[i] = nums[prev] * res[prev]
        
        prev = 1
        for i in range(l-1, -1, -1):
            res[i] *= prev
            prev *= nums[i]
        
        return res
