class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums = sorted(nums)
        delta = []
        for i in range(len(nums) - k + 1):
            delta.append(nums[i + k - 1] - nums[i])
        delta = sorted(delta)
        return delta[0]
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums = sorted(nums)
        res = nums[k - 1] - nums[0]
        for i in range(len(nums) - k + 1):
            res = min(res, nums[i + k - 1] - nums[i])
        return res