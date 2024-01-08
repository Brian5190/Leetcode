class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = [-float('inf')] 
        for i in range(0, len(nums)):
            if nums[i] > l[-1]:
                l.append(nums[i])
            #從中插入
            else:
                for j in range(len(l) - 1, 0, -1): 
                    if l[j] > nums[i] > l[j - 1]:
                        l[j] = nums[i]
                        break
        return len(l) - 1   #扣除inf
