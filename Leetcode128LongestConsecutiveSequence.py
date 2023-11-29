class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        l = []
        for i in range(len(nums)-1):
            if nums[i + 1] - nums[i] != 0:
                l.append(nums[i + 1] - nums[i])
        k = 0
        val = 0
        maxval = 0
        while(k < len(l)):
            if l[k] == 1 :
                val += 1
            else:
                val = 0
            maxval = max(maxval, val)
            k += 1
        return maxval + 1
