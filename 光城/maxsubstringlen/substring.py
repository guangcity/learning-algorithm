class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        MaxLength = 0
        for i in range(len(s)):
            st = ''
            count = 0
            for j in s[i:]:
                if j not in st:
                    st += j
                    count += 1
                    if (MaxLength<count):
                        MaxLength=count
                else:
                    break
        return MaxLength

s = Solution()
str = 'abcdba'
a = s.lengthOfLongestSubstring(str)
print(a)
