class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l1 = len(haystack)
        l2 = len(needle)
        if l2 <= l1:
            for i in range(l1 - l2+1):
                if needle == haystack[i:i+l2]:
                    return i
            return -1
        else:
            return -1