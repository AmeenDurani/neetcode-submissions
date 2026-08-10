class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        prev = 0
        for i, num in enumerate(nums):
            target = 0 - num
            l, r = i + 1, len(nums) - 1

            if num == prev and i != 0:
                continue

            while l < r:
                s = nums[l] + nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    found = [num, nums[l], nums[r]]
                    if found not in res:
                        res.append(found)
                    l += 1
                    r -= 1
            prev = num

        return res