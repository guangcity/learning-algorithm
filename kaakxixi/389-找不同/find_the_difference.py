"""
给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。

 

示例:

输入：
s = "abcd"
t = "abcde"

输出：
e

解释：
'e' 是那个被添加的字母。
"""

"""方法1：直观的想法是使用dict，将每个字符当做键，字符出现的次数当做值，那么两个字典中出现的多出的键或者值不同的键就是所求"""
class Solution(object):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    def findTheDifference(self,s,t):
        dic1 = dict{}
        dic2 = dict{}

        for i  in s:
            dic1[i] = dic1.get(i,0) + 1
        for j in t:
            dic2[j] = dic2.get(j,0) + 1

        for k in dic2:
            if dic1[k] < dic2[k] or k not in dic1:
                return k



"""方法2：实际上是找不同，可以利用数字异或的性质，先把字符转换为数字，再对列表的所有数字进行异或，最后得到的值就是不同的值"""
"""这里注意使用chr()、ord()两个字母数字转换函数，还有map()、reduce()的用法区别"""
class Solution(object):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    def findTheDifference(self,s,t):
        return chr(reduce(operator.xor, map(ord,(s+t))))


    def findTheDifference2(self,s,t):
        res = 0
        for i in(s + t):
            res ^= ord(i)
        return chr(res)




