class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        ls = []
        for i in range(len(nums)):
            if nums[i] not in ls:
                ls.append(nums[i])
                nums[k] = nums[i]
                k += 1
        return k
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] not in nums[i+1 :]:
                nums[k] = nums[i]
                k += 1

        return k
#Best now
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        j = nums[0]
        for i in range(1,len(nums)):
            if nums[i] != j:
                nums[k] = nums[i]
                j = nums[i]
                k += 1

        return k