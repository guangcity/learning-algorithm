class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s_len = len(strs)
        if s_len==0 or strs[0]=="":
            return ""
        if s_len==1:
            return strs[0]
        # 找出最小的字符串长度
        min_lenght = len(min(strs,key=len))
        print(min_lenght)

        # 定义公共前缀长度
        t=0
        # 最小长度循环
        for i in range(min_lenght):
            count = 0
            # 最后一个数与前面所有的数的第i位相比较
            for j in range(s_len):
                if strs[j][i]!=strs[s_len-1][i]:
                    break
                count+=1
            # 判断当前i是否有公共字符，如果有公共字符，此时的count==s_len，否则就小于s_len
            if count<s_len:
                break
            t += 1
        return strs[0][:t]



s = Solution()
str =  ["flower","flow","flight"]
t = s.longestCommonPrefix(str)
print(t)