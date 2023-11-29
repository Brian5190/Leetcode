class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        total = 0
        for i in range(len(a)):
            total += (2 ** (len(a) - i - 1)) * int(a[i])
        for i in range(len(b)):
            total += (2 ** (len(b) - i - 1)) * int(b[i])        
        while(total != 0):
            temp = total % 2
            result += str(temp)
            total = total // 2
        ans = ''
        for i in range(len(result)):
            ans += result[len(result) - i - 1]
        if ans == '':
            return '0'
        return ans