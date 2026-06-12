class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x = []
        for i in range(len(matrix)):
            x.append(matrix[i][len(matrix[0])-1])
        for j in range(len(x)):
            if target <= x[j]:
                for val in matrix[j]:
                    if val == target:
                        return True
        return False
