class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        left = 0
        right = 0
        result = []
        if nums == []:
            return 
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                right = i+1
                if right == len(nums) - 1:
                    result.append(str('%d->%d'%(nums[left],nums[right])))
            else:
                if right == left:
                    result.append(str(nums[i]))
                    
                elif right != left:
                    result.append(str('%d->%d'%(nums[left],nums[right])))
                right = i+1
                left = i+1
        if nums[len(nums) - 1] -nums[len(nums) - 2] != 1:
            result.append(str(nums[len(nums)-1]))
        return result