class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums)
        temp = []
        res = []
        i = 0
        print(nums)
        while i < (len(nums) - 1):
            if i % 3 == 0:
                temp.append(nums[i])
                i += 1
            else:
                if nums[i + 1] - nums[i - 1] <= k:
                    temp.append(nums[i])
                    temp.append(nums[i + 1])
                    i += 2
                    res.append(temp)
                    temp = []
                else:
                    return []
            
        return res