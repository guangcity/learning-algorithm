#!/usr/bin/env python
# coding: utf-8

# # 反转字符串
# 0.说在前面
# 1.反转字符串
# 2.作者的话

# # 0.说在前面
# 非专业人士跨专业自学编程，跟着各位大佬追求进步，从简单的题开始刷，各位莫要嫌弃哈。

# # 1.反转字符串
# 
# 问题
# 
# 编写一个函数，其作用是将输入的字符串反转过来。
# 
# 示例 1:
# 
# 输入: "hello"
# 输出: "olleh"
# 
# 示例 2:
# 
# 输入: "A man, a plan, a canal: Panama"
# 输出: "amanaP :lanac a ,nalp a ,nam A"
# 

# 算法：
# 思想：利用字符串的下标从负一开始进行反转
# 实现：

# In[11]:


def reverseString(s):
    """
    :type s: str
    :rtype: str
     """
    return str(s)[::-1]
    
test1 = 'hello'
test2 ="A man, a plan, a canal: Panama"
print(reverseString(test1))
print(reverseString(test2))


# 分析：
# 字符串[::-1]表示从开始到结束，从后截取
# 

# # 2.作者的话
# 坚持认真学习算法，虽是菜鸟，也会慢慢进步的。
