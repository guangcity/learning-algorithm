class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = 0
        d = {}
        start = 0
        for i in range(len(s)):
            if s[i] in d and start <= d[s[i]] :
                start = d[s[i]] +1
            temp = max(i-start+1,temp)
            d[s[i]] = i
        return temp

## 维护两个字符串，一个是当前最大的字符串l，一个是当前字符串t，最初的时候这两个字符串都为空。每扫一个字符，如果这个字符不在字符串当中，就把当前字符串加上这个字符。如果在，当前字符串就不能再往前加字符了，然后比较当前字符串和当前最大字符串。再把当前字符串的开始地址替换掉因为不能有重复元素，##麻烦
## 滑动窗口！ 机智！
