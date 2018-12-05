class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        return s[::-1]


sl = Solution()
s = "hello"
c = sl.reverseString(s)
print(c)