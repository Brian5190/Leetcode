class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            d[i] = 1 + d.get(i, 0)
        res = ''
        d = sorted(d.items(), key = lambda x: x[1], reverse = True)
        for i in d:
            res += i[0] * i[1]
        return res
        