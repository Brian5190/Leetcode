class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = list(s)
        lt = list(t)
        ls.sort()
        lt.sort()
        return ls == lt
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        d2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in d2:
                d2[t[i]] = 1
            else:
                d2[t[i]] += 1
        return d == d2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        d2 = {}
        if len(s) != len(t):
            return False
        for i in s:
            d[i] = d.get(i,0) + 1
        for i in t:
            d2[i] = d2.get(i,0) + 1
        return d == d2