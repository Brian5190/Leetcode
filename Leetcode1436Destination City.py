class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        res = paths[0][0]
        dic = {}
        for i in paths:
            dic[i[0]] = i[1]
        while res in dic:
            temp = res
            res = dic[res]
            dic.pop(temp)
        return res