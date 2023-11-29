class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        a = a
        b = b
        num1 = []
        num2 = []
        # a >= b
        if a < b:
            temp = b
            b = a
            a = temp

        while (a > 0):
            num1.append(a % 2)
            a = a // 2
        while (b > 0):
            num2.append(b % 2)
            b = b // 2
        while(len(num1) - len(num2) > 0):
            num2.append(0)
        if n > len(num1) or n > len(num2):
            while(n - len(num1) > 0):
                num1.append(1)
            while(n - len(num2) > 0):
                num2.append(1)

        temp = 0
        for i in range(len(num1) - 1, -1, -1):

            if num1[i] + num2[i] == 0 and n - 1 >= i:
                num1[i] = 1
                num2[i] = 1
            elif num1[i] == 1 and num2[i] == 0:
                temp = i
                break
                
        temp = min(n, temp)
        for i in range(temp):
            if num2[i] == 0:
                num2[i] = 1
                num1[i] = (num1[i] + 1) % 2

        tar1 = 0
        tar2 = 0
        for i in range(len(num1)):
            tar1 += num1[i] * 2 ** (i)
            tar2 += num2[i] * 2 ** (i)

        return (tar1 * tar2) % (10 ** 9 + 7)