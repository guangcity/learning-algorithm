class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #预处理
        t='#'+'#'.join(s)+'#'

        RL=[0]*len(t)
        MaxRight=0
        pos=0
        # MaxLen=0
        for i in range(len(t)):
            if i<MaxRight:
                # RL[i]=min(RL[2*pos-i], MaxRight-i)
                j=2*pos-i
                if MaxRight-i>RL[j]:
                    RL[i]=RL[j]
                else:
                    RL[i]=MaxRight-i
            else:
                RL[i]=1
            #尝试扩展，注意处理边界
            while i-RL[i]>=0 and i+RL[i]<len(t) and t[i-RL[i]]==t[i+RL[i]]:
                RL[i]+=1
            #更新MaxRight,pos
            if RL[i] >= RL[pos]:
                MaxRight = RL[i] + i - 1
                pos = i
            '''
                if RL[i]+i-1>MaxRight:
                    MaxRight=RL[i]+i-1
                    pos=i
                #更新最长回文串的长度
                MaxLen=max(MaxLen, RL[i])
            return MaxLen-1
            '''
        a=int((2*pos-MaxRight)/2)
        b=int(MaxRight/2)

        return s[a:b]






s = Solution()
a = s.longestPalindrome('abab')
print(a)