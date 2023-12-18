class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '' or len(s) < len(t):
            return ''

        res = ''
        t_dict = {}
        col_dict = {}
        for i in t:
            t_dict[i] = 1 + t_dict.get(i, 0)
            col_dict[i] = 0
        t_get, left = 0, 0
        res_Len = float('inf')
        for i in range(len(s)):
            if s[i] in col_dict:
                col_dict[s[i]] += 1
                if col_dict[s[i]] == t_dict[s[i]]:
                    t_get += 1
            
            while t_get == len(t_dict):
                if res_Len > i - left + 1:
                    res_Len = i - left + 1
                    res = s[left: i + 1]
                if s[left] in col_dict:
                    col_dict[s[left]] -= 1
                    if t_dict[s[left]] > col_dict[s[left]]:
                        t_get -= 1
                left += 1
        return res
        