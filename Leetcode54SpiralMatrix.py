class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up, right, down, left = 0, 0, len(matrix[0]), len(matrix)
        result = []
        count = len(matrix[0]) * len(matrix)
        while(len(result) < count):
            
            for i in range(up, down):
                result.append(matrix[up][i])
            up += 1
            
            for i in range(right + 1, left):
                result.append(matrix[i][down - 1])
            right += 1

            for i in range(down - 1, up - 1, -1):
                result.append(matrix[left - 1][i - 1])
            down -= 1

            for i in range(left - 2, right - 1, -1):
                result.append(matrix[i][up - 1])
            left -= 1
        return result[: count]
