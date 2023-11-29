
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a in range(len(nums)):
            for b in range(len(nums)) :
                if b > a:
                    if target - nums[b] == nums[a]:
                        return [a,b]
                    