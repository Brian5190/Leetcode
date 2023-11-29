class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip(' ')
        ls = s.split(' ')
        s = ls[len(ls)-1]
        return len(s)