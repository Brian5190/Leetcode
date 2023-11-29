class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        k, s, l = len(nums), 0, 0
        if sum(nums) < target:
            return 0
        for i in range(len(nums)):
            s += nums[i]
            while s >= target and l <= i:
                k = min(k, i-l+1)
                s -= nums[l]
                l += 1
        return k