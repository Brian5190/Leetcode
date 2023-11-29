class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        k = 0
        d = {}
        for r in range(0,len(s)):
            if s[r] not in d:
                d[s[r]] = r
            else:
                l = max(l,d[s[r]] + 1)
                d[s[r]] = r
            k = max(k,r-l+1)
        return k