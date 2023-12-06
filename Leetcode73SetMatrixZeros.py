class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col = []
        row = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    if j not in col:
                        col.append(j)
                    if i not in row:
                        row.append(i)
        for j in col:
            for i in range(len(matrix)):
                matrix[i][j] = 0
        for i in row:
            for j in range(len(matrix[i])):
                matrix[i][j] = 0
