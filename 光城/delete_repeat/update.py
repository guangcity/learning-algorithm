class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        m1 = height[0]
        m2 = height[-1]
        left = 0
        right = len(height) - 1
        ans = min(height[right], height[left]) * (right - left)

        while left < right:
            if m1 >= m2:
                while right > left:
                    if height[right] > m2:
                        m2 = height[right]
                        ans = max(min(height[right], height[left]) * (right - left), ans)
                        if m2 > m1: break
                    right -= 1
            else:
                while right > left:
                    if height[left] > m1:
                        m1 = height[left]
                        ans = max(min(height[right], height[left]) * (right - left), ans)
                        if m1 >= m2: break
                    left += 1

        return ans



