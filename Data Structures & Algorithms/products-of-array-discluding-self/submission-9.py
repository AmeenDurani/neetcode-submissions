class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        l = len(nums)
        left, right, res = [1] * l, [1] * l, [1] * l
        for i in range(l):
            if i == 0:
                continue
            
            prev = i-1
            left[i] = nums[prev] * left[prev]
        
        for i in range(l-1, -1, -1):
            if i == (l-1):
                continue
            
            prev = i + 1
            right[i] = nums[prev] * right[prev]
        
        for i in range(l):
            res[i] = left[i] * right[i]
        
        return res
