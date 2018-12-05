class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        lens = len(matrix)
        for x in range(lens):
            for y in range(lens-x):
                matrix[x][y],matrix[lens-y-1][lens-x-1] = matrix[lens-y-1][lens-x-1],matrix[x][y]
        for p in range(lens):
            for q in range(lens/2):
                matrix[q][p],matrix[lens-1-q][p] = matrix[lens-1-q][p],matrix[q][p]