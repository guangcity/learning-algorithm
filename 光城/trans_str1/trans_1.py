class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        s_len = len(s)

        s1=' '+s
        s=''
        word=0
        print(s1)
        for j in range(1,s_len+1):
            if s1[j]!=' ' and s1[j-1]==' ':
                i=j
                # 防止只有一个字母情况
                if j==s_len:
                    s+=s1[j]
                word += 1
            elif s1[j-1]!=' ' and s1[j]==' ':
                s+=s1[i:j][::-1]
                s+=' '
            elif s1[j]!=' ':
                if j==s_len:
                    s+=s1[i:j+1][::-1]
                continue
            else:
                # 多个空格处理
                s+=' '
        print(word)
        return s
s = Solution()
t = "Let's take LeetCode contest"
m = s.reverseWords(t)
print(m)

print(t[0:3][::-1])