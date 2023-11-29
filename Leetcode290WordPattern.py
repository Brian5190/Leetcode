class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        ls = s.split(' ')
        if len(ls) != len(pattern):
            return False
        if len(set(ls)) != len(set(pattern)):
            return False
        for i in range(len(ls)):
            if pattern[i] not in d:
                d[pattern[i]] = ls[i]
            else:
                if d[pattern[i]] != ls[i]:
                    return False
        return True
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s1 = s.split()
        z = list(zip(pattern,s1))
        if len(pattern) != len(s1):    
            return False
        return (len(set(s1))==len(set(pattern))==len(set(z)))