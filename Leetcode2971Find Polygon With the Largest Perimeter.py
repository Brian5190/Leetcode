class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = list(reversed(sorted(nums)))
        for i in range(len(nums) - 2):
            if nums[i] < sum(nums[i + 1:]):
                return sum(nums[i:])
        return -1
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(len(nums) - 1, 1, -1):
            if nums[i] < sum(nums[:i]):
                return sum(nums[: i + 1])
        return -1