class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        index_List = []
        l = 0
        r = 0
        nums = sorted(nums)
        positive_index = 0

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while(l < r):
                if nums[l] + nums[r] + nums[i] == 0:
                    if [nums[i], nums[l], nums[r]] not in index_List:
                        index_List.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                elif nums[i] + nums[r] + nums[i] < 0:
                    l += 1
        return index_List