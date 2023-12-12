class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = 0
        s_List = list(str(s))
        for i in range(len(s_List)):
            if len(set(s_List[i: i + 3])) == 3:
                res += 1
        return res