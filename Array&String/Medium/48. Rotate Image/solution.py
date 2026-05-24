# 48. Rotate Image
class solution:
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[i].reverse()

        return matrix

rorational = solution()
matrix = [[1,2,3], [4,5,6], [7,8,9]]
new_matirx = rorational.rotate(
    matrix=matrix
)

print(new_matirx)

