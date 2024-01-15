class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls = len(s)
        lt = len(t)
        num = 0
        if ls == 0 :
            return True

        for i in range(lt):
            if s[num] == t[i]:
                num += 1
            if num == ls:
                return True
        return False
