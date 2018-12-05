
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        dict_hight = {}
        i=1
        for index,value in enumerate(height,1):
            dict_hight[index] = value
            i+=1
        print(dict_hight)
        for k in range(1,i):
            for j in range(k+1,i):
                currentArea = (j - k) * min(dict_hight[k], dict_hight[j])
                if currentArea > maxArea:
                    maxArea = currentArea
        return maxArea
s = Solution()
height = [1,8,6,2,5,4,8,3,7]
maxArea = s.maxArea(height)
print(maxArea)
