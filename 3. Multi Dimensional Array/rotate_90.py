def transpose(matrix, n):
	for i in range(n):
		for j in range(i):
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
	return matrix


def inplaceRotate(inputArray, n):
	matrix = transpose(matrix=inputArray, n=n)
	matrix.reverse()
	return matrix

print(inplaceRotate(inputArray=[[1,2,3], [4,5,6], [7,8,9]], n=3))
