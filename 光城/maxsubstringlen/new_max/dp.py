class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 获取字符串的长度
        s_len = len(s)
        # 生成dp算法的二维数组
        dp = [[0] * s_len for i in range(s_len)]
        '''
        分为三种情况：
        第一种:目标子串长度为1;
        第三种:目标子串长度为2;
        第四种:目标子串长度大于等于3; 
        '''
        if s_len == 0:
            return s
        # 最大长度
        maxLen = 1

        # 第一种：检查目标子串长度为1
        i = 0
        while i < s_len:
            dp[i][i] = True
            i += 1

        # 第二种：检查目标子串长度为2
        start = 0
        i = 0
        while i < s_len - 1:
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                maxLen = 2
            i += 1

        # 第三种：检查目标子串长度为大于等于3
        # 遍历长度
        pal_num = 3
        while pal_num <= s_len:
            i = 0
            # 表示循环子串长度为pal_num时,有n-pal_num+1种组合
            while i < (s_len - pal_num + 1):
                # 定义子串末尾
                j = i + pal_num - 1
                # 只有再中间的数为True且两边一样的情况下，才可以将其作为回文子串
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if pal_num > maxLen:
                        start = i
                        maxLen = pal_num
                i += 1
            pal_num += 1
        return s[start:start + maxLen]


