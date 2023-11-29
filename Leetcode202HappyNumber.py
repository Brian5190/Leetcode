class Solution:
    def isHappy(self, n: int) -> bool:
        string = str(n)
        result = 0
        collection = []
        while result != 1 and result not in collection:
            collection.append(result)
            temp = sum(int(digit) ** 2 for digit in string)
            result = temp
            string = str(result)
        if result == 1:
            return True
        return False