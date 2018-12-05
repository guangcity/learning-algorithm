class Solution:
    def longestPalindrome(self,s):
        s_len = len(s)
        s_s = {'0',''}
        for j in range(s_len):
            i = j
            maxlen = 0
            while i>=0:
                if s[i]==s[j] and s[i:j+1] == s[i:j+1][::-1]:
                    if maxlen<j+1-i:
                        maxlen = j+1-i
                        s_s['0']=s[i:j+1]
                i-=1
        return s_s['0']

s = Solution()
a = s.longestPalindrome('abbad')
print(a)

s = 'abcdef'
print(s[::-1])