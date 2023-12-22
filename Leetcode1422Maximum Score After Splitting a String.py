class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        l = []
        for i in s:
            l.append(int(i))
        for i in range(len(s) - 1):
            if l[i] == 0:
                l[i] = 1
            else:
                l[i] = 0
            temp = sum(l)
            if temp > res:
                res = temp
        return res