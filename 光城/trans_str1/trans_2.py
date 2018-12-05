class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        print(s[::-1].split())
        print(s[::-1].split()[::-1])
        print(" ".join(s[::-1].split()[::-1]))
        return " ".join(s[::-1].split()[::-1])

s = Solution()
t = "Let's take LeetCode     contest"
m = s.reverseWords(t)
print(m)

print(t[0:3][::-1])