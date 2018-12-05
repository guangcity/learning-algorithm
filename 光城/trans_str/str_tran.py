class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        new_str = ''
        for i in range(1,len(s)):
            new_str+=s[-i]
        new_str += s[0]
        return new_str


sl = Solution()
s = "hello"
c = sl.reverseString(s)
print(c)