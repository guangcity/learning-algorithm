class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_len = len(s)
        maxcount=0
        s_new = {'0': ''}
        for j in range(s_len):
            for k in range(j,s_len):
                count = 0
                l, m=j, k
                while m >= l:
                    if s[l] == s[m]:
                        l, m = l+1, m-1
                    else:
                        break
                if m < l:
                    count = k - j + 1
                if maxcount < count:
                    maxcount = count
                    s_new['0']=s[j:k+1]
        return s_new['0']

s = Solution()
a = s.longestPalindrome('babd')
print(a)

