class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        s_len = len(s)
        i = 0
        if s_len==0 or s_len==1 or (s_len==2 and s[0]==s[1]):
            return s
        elif s_len==2:
            return s[0]
        sub_s_list = []
        for sub_s in s:
            j = i + 1
            for sub_s1 in s[i + 1:]:
                k = i
                t = j
                if sub_s == sub_s1:
                    while (s[k] == s[t] and k <= t):
                        k += 1
                        t -= 1
                    if k > t:
                        sub_s_list.append(s[i:j+1])
                    if j==s_len:
                        break
                j+=1
            i += 1
        print(sub_s_list)
        ls = {'0':''}
        maxlen=0
        if sub_s_list:
            for i in sub_s_list:
                len1 = len(i)
                if len1 > maxlen:
                    maxlen = len1
                    ls['0'] = i
                    print(ls)
        else:
            ls['0']=s[0]
        return ls['0']

s = Solution()
s1 = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"
a = s.longestPalindrome(s1)
print("--------")
print(a)
