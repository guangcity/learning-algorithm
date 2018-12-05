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



这题考查空间想象，可以想象一个矩阵翻转一个面，然后同时旋转90度，翻转的逆时针90，未翻转的顺时针90

由仿射定理可知这时候将未翻转的翻转过来就是所需的答案。

i,j - 》 （n-1-i,j)->(n-1-j,n-1-i)

