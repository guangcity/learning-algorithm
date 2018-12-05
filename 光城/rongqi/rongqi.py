class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        for i in range(1,len(height)+1):
            for j in range(i,len(height)+1):
                currentArea = (j-i)*min(height[i-1],height[j-1])
                if currentArea>maxArea:
                    maxArea = currentArea

        return maxArea

s = Solution()
height = [1,8,6,2,5,4,8,3,7]
maxArea = s.maxArea(height)
print(maxArea)

