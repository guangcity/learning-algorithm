class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 最终结果
        output_list = []
        # 行index
        down = len(matrix) - 1
        # 列index
        right = len(matrix[0]) - 1
        left = 0  # 左边
        up = 0  # 上边
        while left <= right and up <= down:
            # 左到右
            i = left
            while True:
                if i > right:
                    break
                output_list.append(matrix[up][i])
                i += 1
            # 行下移
            up += 1
            # 上到下
            j = up
            while True:
                if j > down:
                    break
                output_list.append(matrix[j][right])
                j += 1
            # 列左移
            right -= 1
            # 右到左
            p = right
            if (up <= down):
                while True:
                    if p < left:
                        break
                    # print(matrix[down][p])
                    output_list.append(matrix[down][p])
                    p -= 1
                    # print("----------")
                # 行上移
            down -= 1
            # 下到上
            q = down
            if (left <= right):
                while True:
                    if q < up:
                        break
                    # print(matrix[q][left])
                    output_list.append(matrix[q][left])
                    q -= 1
            left += 1


        return output_list
s = Solution()
m = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
t = s.spiralOrder(m)
print(t)