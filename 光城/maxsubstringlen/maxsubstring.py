class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = MaxLength = 0
        hash_str = {}
        for index,char in enumerate(s):
            if char in hash_str and start<=hash_str[char]:
                start = hash_str[char]+1
            else:
                if(MaxLength<(index-start+1)):
                    MaxLength=index-start+1
            hash_str[char] = index

        return MaxLength

s = Solution()
str = 'abcdba'
a = s.lengthOfLongestSubstring(str)
print(a)



