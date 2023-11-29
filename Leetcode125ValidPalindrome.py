class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = ''
        s = s.lower()
        for i in range(len(s)):
            if ord(s[i]) in range(97,123) or (ord(s[i]) in range(48,58)):
                ls += s[i]
        lens = len(ls)
        for i in range(len(ls)):
            if ls[i] != ls[lens-1-i]:
                return False
        return True