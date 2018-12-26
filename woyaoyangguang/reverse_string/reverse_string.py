'''编写一个函数，其作用是将输入的字符串反转过来。
示例 1:

输入: "hello"
输出: "olleh"

示例 2:

输入: "A man, a plan, a canal: Panama"
输出: "amanaP :lanac a ,nalp a ,nam A"
'''



'''
思路：
将字符串转化为列表,利用列表将顺序逆序，然后通过join函数,
将列表转化为字符串
'''

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=list(s)[::-1]
        res=''.join(l)
        return res




