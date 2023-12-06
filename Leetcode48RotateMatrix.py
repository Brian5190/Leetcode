class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = [[0] * len(matrix) for i in range(len(matrix))]

        for i in range(len(matrix)):
            
            for j in range(len(matrix)):
                l[i][j] = matrix[j][i]
        
        for i in l:
            i.reverse()
        
        for i in range(len(matrix)):
            
            for j in range(len(matrix)):
                matrix[i][j] = l[i][j]
        

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            left, right = 0, len(matrix) - 1
            
            while left < right : 
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in matrix:
            i = i.reverse()