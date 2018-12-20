class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=0:
            res = int(str(x)[::-1])
            if -2**31 <= res <=2**31-1 :
                return res
            else:
                return 0
        else:
            res = int(str(abs(x))[::-1])#非纯数字组成的字符串转换问题
            if res<=2**31-1:
                return -res
            else:
                return 0
