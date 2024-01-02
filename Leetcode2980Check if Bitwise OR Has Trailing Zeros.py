class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        temp = 0
        for i in nums:
            if i % 2 == 0:
                temp += 1
        if temp >= 2:
            return True
        return False