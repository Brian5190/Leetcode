class Solution:
    def minAnagramLength(self, s: str) -> int:
        d = {}
        for i in s:
            d[i] = 1 + d.get(i, 0)
        l = list(d.values())

        m = 1000000
        t = min(l)
        for i in range(1, t + 1):
            temp = 0
            for j in l:
                if j % i != 0:
                    temp = 1
                    break
            if temp == 0:
                m = min(m,(sum(l) // i))

        return m