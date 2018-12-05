class Solution:
    def generateMatrix(self, n):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 最终结果
        output_list = [([0] * n) for i in range(n)]
        # 行index
        down = n-1
        # 列index
        right = n-1
        left = 0  # 左边
        up = 0  # 上边
        value = 1
        while left <= right and up <= down:
            # 左到右
            i = left
            while True:
                if i > right:
                    break
                output_list[up][i]=value
                i += 1
                value+=1
            # 行下移
            up += 1
            # 上到下
            j = up
            while True:
                if j > down:
                    break
                output_list[j][right] = value
                j += 1
                value+=1
            # 列左移
            right -= 1
            # 右到左
            p = right
            if (up <= down):
                while True:
                    if p < left:
                        break
                    # print(matrix[down][p])
                    output_list[down][p] = value
                    p -= 1
                    value+=1
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
                    output_list[q][left] = value
                    q -= 1
                    value+=1
            left += 1
        return output_list
s = Solution()
m = 3
t = s.generateMatrix(m)
print(t)