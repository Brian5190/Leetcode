class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        count = {}
        res, j = 0, 0
        for i in nums:
            count[i] = 0
        for i in nums:
            count[i] += 1
            while count[max_val] >= k:
                count[nums[j]] -= 1
                j += 1
            res += j
        return res