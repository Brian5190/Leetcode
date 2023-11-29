class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fromLeft = [1] * len(nums)
        fromRight = [1] * len(nums)
        for i in range(1,len(nums)):
            fromLeft[i] = fromLeft[i-1] * nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            fromRight[i] = fromRight[i+1] * nums[i+1]
        for i in range(len(nums)):
            nums[i] = fromRight[i] * fromLeft[i]
        return nums