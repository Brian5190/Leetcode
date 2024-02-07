class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = -1
        l = []
        for i in range(len(s)):
            if s[i] not in s[i + 1: len(s)] and s[i] not in l:
                return i
            if s[i] in s[i + 1: len(s)]:
                l.append(s[i])
        return res
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s:
            d[i] = 1 + d.get(i, 0)
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s[i] not in s[i + 1: len(s)] and s[i] not in s[0: i]:
                return i
        return -1