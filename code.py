class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]):
        def length(z):
            if z not in memo:
                memo[z] = 1 + max([length(Z)
                                   for Z in [z+1, z-1, z+1j, z-1j]
                                   if Z in matrix and matrix[z] > matrix[Z]]
                                  or [0])
            return memo[z]
        memo = {}
        matrix = {i + j*1j: val
                  for i, row in enumerate(matrix)
                  for j, val in enumerate(row)}
        return max(map(length, matrix), default = 0)





