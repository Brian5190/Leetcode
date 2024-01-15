class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = {}
        for i in matches:
            d[i[0]] = d.get(i[0], 0)
        for i in matches:
            d[i[1]] = 1 + d.get(i[1], 0)
        res = [[], []]
        for i in d:
            if d[i] == 0:
                res[0].append(i)
            if d[i] == 1:
                res[1].append(i)
        for l in res:
            l = l.sort()
        return res