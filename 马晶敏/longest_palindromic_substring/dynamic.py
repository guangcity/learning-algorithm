class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_len=len(s)
        if(s_len==0):
            return s
        maxL=1
        startI=s_len-1
        mat=[[0]* s_len for i in range(s_len)]
        for i in range(s_len):
            mat[i][i]=True            
        for i in range(s_len-1):
            if(s[i]==s[i+1]):
                maxL=2
                startI=i
                mat[i][i+1]=True
            else:
                mat[i][i+1]=False
        for i in range(2,s_len):
            for j in range(0,s_len-i):
                if(s[j]==s[j+i] and mat[j+1][j+i-1]):
                    maxL=i+1
                    startI=j
                    mat[j][j+i]=True
                else:
                    mat[j][j+i]=False
        return s[startI:startI+maxL]
        
            