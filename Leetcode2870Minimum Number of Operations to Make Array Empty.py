class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d = {}
        res = 0
        for i in nums:
            d[i] = 1 + d.get(i, 0) # build dictionary with key = number and value = count
        for i in d:
            if d[i] < 2:
                return -1
            res += ceil(d[i] / 3) # ceil(k) = j with j is integer and |j - k| < 1 
        return res
                