matrix = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(matrix)):
	for j in range(i):
		matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print(matrix)


for i in range(len(matrix)):
    left, right = 0, len(matrix) - 1
	
    while left < right : 
        matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
        left += 1
        right -= 1

print(matrix)