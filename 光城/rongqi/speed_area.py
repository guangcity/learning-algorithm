

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea=0
        low = 0
        high = len(height)-1
        while low<high:
            currentArea = (high - low) * min(height[high], height[low])
            if currentArea > maxArea:
                maxArea = currentArea
            if height[high]>height[low]:
                low+=1
            else:
                high-=1
        return maxArea
s = Solution()
height = [1,8,6,2,5,4,8,3,7]
maxArea = s.maxArea(height)
print(maxArea)
