class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        l = []
        for i in range(len(bank)):
            bank[i] = sum(int(j) for j in list(bank[i]))
        for i in range(len(bank)):
            if bank[i] != 0:
                l.append(bank[i])
        if len(l) > 1:
            a = l[0]
            for i in range(1, len(l)):
                res += a * l[i]
                a = l[i]
        return res
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        l = []
        for i in range(len(bank)):
            temp = bank[i].count('1')
            if temp > 0:
                l.append(temp)
        for i in range(len(l) - 1):
            res += l[i] * l[i + 1]
        return res