class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l<=1:
            return s
        # 定义最长回文串
        long_palindrome = ''
        for i in range(l-1):

            p1 = self.center_expand(s,i,i)
            if len(p1)>len(long_palindrome):
                long_palindrome=p1
            p2 = self.center_expand(s,i,i+1)
            if len(p2)>len(long_palindrome):
                long_palindrome=p2
        return long_palindrome
    def center_expand(self,s,left,right):
        s_len = len(s)
        while left>=0 and right<s_len and s[left]==s[right]:
            left-=1
            right+=1
        # 上述循环后,left与right是不相等的字符，所以截取字符串,是letf+1,right
        return s[left+1:right]
s = Solution()
a = s.longestPalindrome('abab')
print(a)