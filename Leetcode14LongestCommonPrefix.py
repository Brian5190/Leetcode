class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ''
        minL = len(strs[0])
        for i in strs:
            if minL > len(i):
                minL = len(i)
        for i in range(minL):
            k = 0
            q = 0
            for j in range(len(strs)-1):
                if strs[j][i] == strs[j+1][i]:
                    k += 1
                else:
                    q = -1
                    break
            if q == -1:
                break

            if k == len(strs) - 1:
                s = s + strs[0][i]                
        return s

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ''
        x= sorted(strs)

        for i in range( min(len(x[0]),len(x[-1])) ):
            if x[0][i] == x[-1][i]:
                s = s + x[0][i]
            else:
                return s
        return s