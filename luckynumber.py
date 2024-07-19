from typing import List

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        min_array = [min(row) for row in matrix]  # Find the minimum values in each row
        max_array = [max(col) for col in zip(*matrix)]  # Find the maximum values in each column

        lucky = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == min_array[i] and matrix[i][j] == max_array[j]:
                    lucky.append(matrix[i][j])
        
        return lucky
