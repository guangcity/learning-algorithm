class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        count = 0
        for i in zip(*strs):
            print(i)
            if len(set(i)) == 1:
                count += 1
            else:
                return strs[0][:count]
        return strs[0][:count]



s = Solution()
str =  ["flower","flow","flight"]
t = s.longestCommonPrefix(str)
print(t)