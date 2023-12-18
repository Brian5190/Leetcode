class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        num_dic = {}
        res = []
        for i in range(len(grid) ** 2):
            num_dic[i + 1] = 0
        for i in grid:
            for j in i:
                num_dic[j] += 1
                if num_dic[j] > 1:
                    res.append(j)
        for i in num_dic:
            if num_dic[i] == 0:
                res.append(i)
        
        return res