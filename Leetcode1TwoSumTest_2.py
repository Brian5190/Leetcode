class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for a in range(len(nums)):
            dic[nums[a]] = a
        for b in range(len(nums)):
            c = target - nums[b]
            if c in dic and dic[c] != b:
                return [b ,dic[c]]