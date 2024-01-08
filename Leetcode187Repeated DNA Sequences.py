class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = {}
        for i in range(len(s) - 9):
            if s[i: i + 10] in d:
                d[s[i: i + 10]] += 1
            else:
                d[s[i: i + 10]] = 1
        return [i for i in d if d[i] >= 2]