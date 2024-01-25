class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #DP
        res = [0] * len(text1)
        for s in text2:
            temp = 0
            for i in range(len(text1)):
                if temp < res[i]:
                    temp = res[i]
                elif s == text1[i]:
                    res[i] = temp + 1
               # print('res = ', res, 'temp = ', temp, 's = ', s, 'text1 = ', text1[i])
        return max(res)