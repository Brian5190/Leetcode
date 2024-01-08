class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d = {}
        res =[]
        for i in nums:
            d[i] = 1 + d.get(i, 0)
        print(d)
        while(max(d.values()) > 0):
            temp = []
            for i in d:
                if d[i] > 0:
                    temp.append(i)
                    d[i] -= 1
            res.append(temp)
        return res