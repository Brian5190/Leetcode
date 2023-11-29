class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            k = 1
            l = 0
            for i in range(n):
                temp = k
                k = k + l
                l = temp

            return k
class Solution:
    def climbStairs(self, n: int) -> int:
        ls = [1,0,0]
        for i in range(n):
            ls[2] = ls[0]
            ls[0] = ls[0] + ls[1]
            ls[1] = ls[2]

        return ls[0]