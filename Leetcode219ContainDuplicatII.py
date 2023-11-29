class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        for i in range(len(nums)):
            temp = min(k,len(nums)-i)
            if nums[i] in nums[i+1:i+1+temp]:
                return True
        return False
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        k = min(k, len(nums))
        for i in range(len(nums) - k):
            if nums[i] in nums[i + 1: i + k + 1]:
                return True
        for i in range(len(nums) - k, len(nums)):
            if nums[i] in nums[i + 1: len(nums)]:
                return True
        return False
