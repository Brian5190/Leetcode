class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = []
        if numRows == 1:
            return s
        if numRows == 0:
            return ''
        for i in range(numRows):
            result.append([])
        for i in range(len(s)):
            k = i % (numRows + numRows - 2)
            print(k, i, s[i])
            if k < numRows:
                result[k].append(s[i])
            if k >= numRows:
                k = k % numRows
                result[numRows - k - 2].append(s[i])
        ans = ''
        for i in result:
            ans += ''.join(i)
        return ans