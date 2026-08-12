class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        mid = (right + left) // 2

        while left != right:
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
            mid = (right + left) // 2

        return nums[mid]
