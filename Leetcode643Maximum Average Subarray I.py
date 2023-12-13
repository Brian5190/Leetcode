class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = temp = sum(nums[: k])        
        i = 0
        while (i < len(nums) - k):
            temp = temp - nums[i] + nums[i + k]
            if temp > res:
                res = temp
            i += 1
        return res / k