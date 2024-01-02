class Solution:
    def maximumLength(self, s: str) -> int:
        s_Len = len(s)
        d = {s[0]: 1}
        temp = [0]
        for i in range(1, s_Len):

            temp.append(i)
            if s[temp[-1]] == s[temp[-2]]:
                for j in range(len(temp) - 1, -1, -1):
                    if s[temp[j]: i + 1] in d:
                        d[s[temp[j]: i + 1]] += 1
                    else:
                        d[s[temp[j]: i + 1]] = 1
            else:
                if s[i] in d:
                    d[s[i]] += 1
                else:
                    d[s[i]] = 1
                temp = [i]
        res = -1
        for i in d:
            if d[i] >= 3:
                res = max(len(i), res)
        return res