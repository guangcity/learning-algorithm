class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        t = list(s)
        i=0
        j=len(s)-1
        while i<j:
            temp = t[i]
            t[i]=t[j]
            t[j]=temp
            i+=1
            j-=1

        return ''.join(t)


sl = Solution()
s = ""
c = sl.reverseString(s)
print(c)