class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d = {}
        res = 0
        for i in nums:
            d[i] = 1 + d.get(i, 0)
        for i in d:
            if d[i] < 2:
                return -1
            res += ceil(d[i] / 3)
        return res
                