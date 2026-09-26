class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array, nlog(n) time complexity
        nums = sorted(nums)

        res = []
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] > -1 * nums[i]:
                    r -= 1
                elif nums[l] + nums[r] < -1 * nums[i]:
                    l += 1
                else:
                    if [nums[i], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
        
        return res
